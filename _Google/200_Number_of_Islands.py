# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 07:53:24 2016

200. Number of Islands

Total Accepted: 35558 Total Submissions: 133900 Difficulty: Medium

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. 
An island is surrounded by water and is formed by connecting adjacent lands horizontally or 
vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

11110
11010
11000
00000
Answer: 1

Example 2:

11000
11000
00100
00011
Answer: 3

@author: Jamie
"""

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid)==0 or len(grid[0])==0: return 0
        m, n = len(grid), len(grid[0])
    
        def explore_and_mark(i,j):
            if grid[i][j] == '1':
                grid[i][j] = '#'
                if i+1<=m-1: explore_and_mark(i+1,j)
                if i-1>=0  : explore_and_mark(i-1,j)
                if j+1<=n-1: explore_and_mark(i,j+1)
                if j-1>=0  : explore_and_mark(i,j-1)
                return True
            else:
                return False
        
        res = 0
        for i in range(m):
            for j in range(n):
                if explore_and_mark(i,j): res +=1
        
        return res
