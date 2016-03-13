# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 12:05:50 2016

221. Maximal Square My Submissions Question
Total Accepted: 23997 Total Submissions: 105183 Difficulty: Medium
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing all 1's and return its area.

For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Return 4.
Credits:

*** DP 的思路， 从右下往左上走
*** 

@author: Jamie
"""

class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if matrix == []: return 0
        m,n = len(matrix), len(matrix[0])
        
        dp = [[0]*n for x in xrange(m) ]
        res = 0
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if i == m-1 or j == n-1: dp[i][j] = int(matrix[i][j])
                elif matrix[i][j] == '0': dp[i][j] = 0
                else: dp[i][j] = min(dp[i+1][j],dp[i][j+1],dp[i+1][j+1]) + 1
                res = max(res, dp[i][j])
        return res**2
                    
sol = Solution()
print sol.maximalSquare([['1']])