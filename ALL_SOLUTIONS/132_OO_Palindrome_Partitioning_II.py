# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 09:40:50 2016

132. Palindrome Partitioning II My Submissions Question
Total Accepted: 45765 Total Submissions: 216151 Difficulty: Hard
Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

For example, given s = "aab",
Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.

解题思路：由于这次不需要穷举出所有符合条件的回文分割，而是需要找到一个字符串s回文分割的最少分割次数，
分割出来的字符串都是回文字符串。求次数的问题，不需要dfs，用了也会超时，之前的文章说过，
求次数要考虑动态规划（dp）。对于程序的说明：p[i][j]表示从字符i到j是否为一个回文字符串。
dp[i]表示从第i个字符到最后一个字符，最少的分割次数下，有多少个回文字符串，即分割次数+1。
这道题动态规划的思路比较简单，直接上代码吧。

@author: zeminzhang
"""

class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        if length <=1: return 0
        
        dp = [length-x for x in range(length+1)]
        p = [[False for x in range(length)] for y in range(length)]
        
        for i in range(length-1,-1,-1):
            for j in range(i,length):
                if s[i] == s[j] and ( (j-i)<2 or p[i+1][j-1] ):
                    p[i][j] = True
                    dp[i] = min(dp[i],1+dp[j+1])
        
        return dp[0]-1