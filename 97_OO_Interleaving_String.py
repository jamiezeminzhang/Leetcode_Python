# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 21:12:51 2016

97. Interleaving String My Submissions Question
Total Accepted: 44764 Total Submissions: 203953 Difficulty: Hard
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

For example,
Given:
s1 = "aabcc",
s2 = "dbbca",

When s3 = "aadbbcbcac", return true.
When s3 = "aadbbbaccc", return false.

解题思路：动态规划。dp[i][j]表示s1[0...i-1]和s2[0...j-1]是否可以拼接为s3[0...i+j-1]，
可以拼接为true，不可以拼接为false。


@author: zeminzhang
"""

class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        length1, length2, length3 = len(s1),len(s2),len(s3)
        if length3 != length1 + length2: return False
        dp = [[False for x in range(length2+1)] for y in range(length1+1)]
        dp[0][0] = True
        for i in range(1,length1+1):
            dp[i][0] = (dp[i-1][0] and s1[i-1] == s3[i-1])
        for j in range(1,length2+1):
            dp[0][j] = (dp[0][j-1] and s2[j-1] == s3[j-1])
        for i in range(1,length1+1):
            for j in range(1,length2+1):
                dp[i][j] = (dp[i-1][j] and s1[i-1]==s3[i+j-1]) or (dp[i][j-1] and s2[j-1]==s3[i+j-1])
        
        return dp[length1][length2]