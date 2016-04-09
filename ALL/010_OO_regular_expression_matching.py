# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 10:00:45 2015

LeetCdoe #10 Regular Expression Matching

Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true


@author: zzhang


This one is the algorithm provided by the editor. Java and C++ works under this
algorithm, but Python not. So we using a dynamic programming method for Python


先来看递归的解法：

如果P[j+1]!='*'，S[i] == P[j]=>匹配下一位(i+1, j+1)，S[i]!=P[j]=>匹配失败；

如果P[j+1]=='*'，S[i]==P[j]=>匹配下一位(i+1, j+2)或者(i, j+2)，S[i]!=P[j]=>匹配下一位(i,j+2)。

匹配成功的条件为S[i]=='\0' && P[j]=='\0'。


class Solution:
    # @param {string} s
    # @param {string} p
    # @return {boolean}
    def isMatch(self, s, p):
        if not p:
            return not s
        if not s:
            return False
        return self.is_match_aux(s,p,0,0)
    
    def is_match_aux(self,s,p,si,pi):
        if pi == len(p):
            return si == len(s)
        
        # Next char is not *
        # pi may be the last char
        if pi<len(p)-1 and p[pi+1] != '*' or pi == len(p) -1:
            assert p[pi] != '*'
            # si must be in bound
            is_cur_matched = si<len(s) and (p[pi] == s[si] or p[pi] == '.')
            is_next_matched = self.is_match_aux(s,p,si+1,pi+1)
            return is_cur_matched and is_next_matched
        
        # Next char is *
        while si<len(s) and pi< len(p) and (p[pi]==s[si] or p[pi]=='.'):
            if self.is_match_aux(s,p,si,pi+2):
                return True
            si += 1
        return self.is_match_aux(s,p,si,pi+2)
        

==============OR====================
class Solution:
    # @return a boolean
    def isMatch(self, s, p):
        if len(p)==0: return len(s)==0
        if len(p)==1 or p[1]!='*':
            if len(s)==0 or (s[0]!=p[0] and p[0]!='.'):
                return False
            return self.isMatch(s[1:],p[1:])
        else:
            i=-1; length=len(s)
            while i<length and (i<0 or p[0]=='.' or p[0]==s[i]):
                if self.isMatch(s[i+1:],p[2:]): return True
                i+=1
            return False
            
        
=================DP===========================
http://www.makuiyu.cn/2015/01/LeetCode_10.%20Regular%20Expression%20Matching/

思路是使用bool类型的二维数组dp[m+1][n+1]（m、n分别为字符串s和p的长度）记录s和p是否匹配，
即dp[i+1][j+1]表示s的前i个字符是否与p的前j的字符相匹配。

如果p[j]不等于'*'，则dp[i + 1][j + 1] = dp[i][j] && s[i] == p[j]

如果p[j]等于'*'，则当且仅当在下面三种情况为真，dp[i + 1][j + 1]为真：

    '*'前面字符重复出现0次，则p字符串需要往前看2位，即dp[i + 1][j - 1]是否为真

    '*'前面的字符重复出现1次，则p字符串只需要往前看1位，即dp[i + 1][j]是否为真

    '*'前面的字符重复出现次数大于1次，则s字符串需要往前看1位，即dp[i][j + 1]是否为真，
    以及s字符串当前字符（s[i]）与p字符串'*'前面字符（p[j - 1]）是否相匹配。

注意，'.'可以与任意单个字符匹配。

注：动态规划思路是参考的这里。这里将空间复杂度降低到了O(n)，有兴趣的可以看看。

时间复杂度：O(mn)

空间复杂度：O(mn)

"""

class Solution:
    # @return a boolean
    def isMatch(self, s, p):
        dp=[[False for i in range(len(p)+1)] for j in range(len(s)+1)]
        dp[0][0]=True
        for i in range(1,len(p)+1):
            if p[i-1]=='*':
                if i>=2:
                    dp[0][i]=dp[0][i-2] or dp[0][i-1]# 包括i-1那个位置的字符都不重复，重复0次。
        for i in range(1,len(s)+1):
            for j in range(1,len(p)+1):
                if p[j-1]=='.':
                    dp[i][j]=dp[i-1][j-1]
                elif p[j-1]=='*':
                    dp[i][j]=dp[i][j-1] or dp[i][j-2] or (dp[i-1][j] and (s[i-1]==p[j-2] or p[j-2]=='.'))
                else:
                    dp[i][j]=dp[i-1][j-1] and s[i-1]==p[j-1]
        return dp[len(s)][len(p)]
    

