# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 10:52:10 2016

140. Word Break II My Submissions Question
Total Accepted: 50223 Total Submissions: 262887 Difficulty: Hard
Given a string s and a dictionary of words dict, add spaces in s to construct 
a sentence where each word is a valid dictionary word.

Return all such possible sentences.

For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].

A solution is ["cats and dog", "cat sand dog"].

解题思路：这道题不只像word break那样判断是否可以分割，而且要找到所有的分割方式，
那么我们就要考虑dfs了。不过直接用dfs解题是不行的，为什么？因为决策树太大，如果全部遍历一遍，
时间复杂度太高，无法通过oj。那么我们需要剪枝，如何来剪枝呢？使用word break题中的动态规划的结果，
在dfs之前，先判定字符串是否可以被分割，如果不能被分割，直接跳过这一枝。实际上这道题是dp+dfs。

@author: zeminzhang
"""

class Solution(object):
    def check(self, s, wordDict):
        length = len(s)
        dp = [False for x in range(length+1)]
        dp[0] = True
        for i in range(1,length+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
        return dp[length]
    
    def dfs(self,s,wordDict, s_string):
        if self.check(s, wordDict):
            if len(s) == 0: Solution.res.append(s_string)
            else:
                for i in range(1,len(s)+1):
                    if s[:i] in wordDict:
                        if s_string == '':
                            self.dfs(s[i:], wordDict, s_string+s[:i])
                        else:
                            self.dfs(s[i:], wordDict, s_string+' '+s[:i])
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        Solution.res = []
        self.dfs(s, wordDict,'')
        return Solution.res
    