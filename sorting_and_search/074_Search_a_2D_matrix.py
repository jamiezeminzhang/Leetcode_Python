# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 23:24:15 2016

74. Search a 2D Matrix

Total Accepted: 83210 Total Submissions: 243134 Difficulty: Medium

Write an efficient algorithm that searches for a value in an m x n matrix. 
This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return true.

@author: zeminzhang
"""

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m, n = len(matrix), len(matrix[0])
        if m==0 or n==0: return False
        if target<matrix[0][0] or target>matrix[-1][-1]: return False
        
        up, down = 0, m-1
        while up<=down:
            center = (up+down)/2
            if matrix[center][0] == target: return True
            elif matrix[center][0]<target:
                up = center + 1
            else: down = center-1

        left, right = 0, n-1
        while left<=right:
            mid = (left+right)/2
            if matrix[down][mid] == target: return True
            elif matrix[down][mid]<target:
                left = mid +1
            else: right = mid-1
        return False
        