# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 09:35:47 2016

139. Word Break
Total Accepted: 77066 Total Submissions: 315805 Difficulty: Medium

Given a string s and a dictionary of words dict, determine if s can be segmented 
into a space-separated sequence of one or more dictionary words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".

*** 如果只需要一个true false / 活着需要你return一共又多少组解，只要数字的话
用dfs 一般会超时
所以一般用dp
@author: zeminzhang
"""
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        length = len(s)
        dp = [True] + [False for _ in range(length)]
        for i in range(length+1):
            for word in wordDict:
                if dp[i] and s[i:].startswith(word):
                    dp[i+len(word)] = True
        return dp[-1]
