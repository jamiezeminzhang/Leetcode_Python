# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 21:58:47 2016

118. Pascal's Triangle My Submissions Question
Total Accepted: 72502 Total Submissions: 224665 Difficulty: Easy
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

@author: zeminzhang
"""

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = [[1 for x in range(1,y+2)] for y in range(numRows)]
        if numRows <= 2: return res
        for row in range(2,numRows):
            for col in range(1,row):
                res[row][col] = res[row-1][col-1] + res[row-1][col]
        return res