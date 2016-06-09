# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 07:04:57 2016

64. Minimum Path Sum

Total Accepted: 73213 Total Submissions: 207753 Difficulty: Medium

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

@author: zeminzhang
"""

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m,n = len(grid), len(grid[0])
        for i in range(1,m):
            grid[i][0] += grid[i-1][0]
        for i in range(1,n):
            grid[0][i] += grid[0][i-1]
        for i in range(1,m):
            for j in range(1,n):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1]) 
        return grid[m-1][n-1]