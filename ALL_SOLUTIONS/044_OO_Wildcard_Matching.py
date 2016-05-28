# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 10:46:45 2016

44. Wildcard Matching

Total Accepted: 56298 Total Submissions: 321910 Difficulty: Hard

Implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "*") → true
isMatch("aa", "a*") → true
isMatch("ab", "?*") → true
isMatch("aab", "c*a*b") → false

解题思路：管他什么吊巧妙解法。这种题一律dp。稳稳可以做。

*******************************************************

本来的解法写的是2维DP，但是最长的test老是TLE。个人以为如果面试的话给出2维DP更好，因为思路更清晰。
附上2维DP TLE的代码
class Solution(object):
    def isMatch(self, s, p):
        dp = [ [False for x in range(len(p)+1)] for y in range(len(s)+1) ]
        dp[0][0] = True
        
        for i in range(1,len(s)+1):
            for j in range(1,len(p)+1):
                if p[j-1] == '?' or p[j-1] == s[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    for k in range(j,-1,-1):
                        if dp[i-1][k] == True:
                            dp[i][j] = True
                            break
        return dp[len(s)][len(p)]

@author: zeminzhang
"""

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
		
	dp[n] means the whether substring s[:n] matches the pattern until i
        dp[0] means the empty string '' or s[:0] which only match the pattern '*'
        use the reversed builtin because for every dp[n+1] we use the previous 'dp'
	每一次dp用的都是上一轮dp的结果
	逆序那里的考虑是：每次都从s的最后一个字符开始考虑匹配。对于现在的字符i，如果s最后一个字符与i匹配，
	并且上一次dp的结果与i的上一个字符匹配，那么现在的结果就匹配。
		
	如果i是*，那么从dp的任何一个true开始，后面统统都是true。
        
	"""
        length = len(s)
        dp = [True]+[False for x in range(length)]
        for i in p:
            if i!='*':
                for j in range(length-1,-1,-1):
                    dp[j+1] = dp[j] and (s[j]==i or i=='?')
            else:
                for j in range(1,length+1):
                    dp[j] = dp[j-1] or dp[j]
            dp[0] = dp[0] and i=='*'
        return dp[-1]
