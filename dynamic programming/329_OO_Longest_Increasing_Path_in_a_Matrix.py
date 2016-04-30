# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 20:57:46 2016

329. Longest Increasing Path in a Matrix My Submissions Question

Total Accepted: 7448 Total Submissions: 24902 Difficulty: Medium
Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down. 
You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

Example 1:

nums = [
  [9,9,4],
  [6,6,8],
  [2,1,1]
]
Return 4
The longest increasing path is [1, 2, 6, 9].

Example 2:

nums = [
  [3,4,5],
  [3,2,6],
  [2,2,1]
]
Return 4
The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.

        
@author: Jamie
"""

class Solution(object):
    def longestIncreasingPath(self, matrix):

        if not matrix: return 0
        m, n = len(matrix), len(matrix[0])
        
        sorted_matrix = sorted([(i, j, val)
                        for i, row in enumerate(matrix)
                        for j, val in enumerate(row)],
                        key = operator.itemgetter(2))
        
        dp = [[1]*n for j in range(m)]
        for x, y, val in sorted_matrix:
            for dx, dy in zip([0,1,0,-1],[1,0,-1,0]):
                nx, ny = x+dx, y+dy
                if 0<=nx<m and 0<=ny<n and matrix[x][y]>matrix[nx][ny]:
                    dp[x][y] = max(dp[x][y], dp[nx][ny]+1 )
        print dp
        return max([max(x) for x in dp])