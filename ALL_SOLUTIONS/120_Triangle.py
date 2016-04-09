# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 22:57:46 2016

120. Triangle My Submissions Question
Total Accepted: 61702 Total Submissions: 210946 Difficulty: Medium
Given a triangle, find the minimum path sum from top to bottom. Each step you 
may move to adjacent numbers on the row below.

For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:
Bonus point if you are able to do this using only O(n) extra space, where n is 
the total number of rows in the triangle.

@author: zeminzhang
"""

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        
        length = len(triangle)
        if length == 0: return 0
        if length == 1: return triangle[0][0]
        lis = [triangle[0][0]+triangle[1][0], triangle[0][0]+triangle[1][1]]
        if length == 2: return min(lis)
        for i in range(2,length):
            lis.insert(0,lis[0]+triangle[i][0])
            for j in range(1,i):
                lis[j] = min(lis[j],lis[j+1]) + triangle[i][j]
            lis[i] = lis[i]+triangle[i][i]
        
        return min(lis)