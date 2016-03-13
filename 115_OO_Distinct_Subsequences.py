# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 04:38:44 2016

115. Distinct Subsequences My Submissions Question

Total Accepted: 46435 Total Submissions: 165070 Difficulty: Hard
Given a string S and a string T, count the number of distinct subsequences of T in S.

A subsequence of a string is a new string which is formed from the original 
string by deleting some (can be none) of the characters without disturbing the 
relative positions of the remaining characters. (ie, "ACE" is a subsequence of 
"ABCDE" while "AEC" is not).

Here is an example:
S = "rabbbit", T = "rabbit"

Return 3.

##################

这道题使用动态规划来解决。题的意思是：S的所有子串中，有多少子串是T。
下面来看看状态转移方程。dp[i][j]表示S[0...i-1]中有多少子串是T[0...j-1]。

当S[i-1]=T[j-1]时：dp[i][j]=dp[i-1][j-1]+dp[i-1][j]；S[0...i-1]中有多少子串是
T[0...j-1]包含：{S[0...i-2]中有多少子串是T[0...j-2]}+{S[0...i-2]中有多少子串是T[0...j-1]}

当S[i-1]!=T[j-1]时：dp[i][j]=dp[i-1][j-1]

那么初始化状态如何确定呢：dp[i][0]=1；S[0...i-1]只有一个子串是空串。



@author: zeminzhang
"""
class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        length_s, length_t = len(s), len(t)
        # dp[i][j] represents the number of distinct subsequences of T[:j] in S[:i]
        dp = [[0 for x in range(length_t+1)] for y in range(length_s+1)]
        for i in range(length_s+1):
            dp[i][0] = 1
        for i in range(1,length_s+1):
            for j in range(1,length_t+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j] # very important here
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[length_s][length_t]
