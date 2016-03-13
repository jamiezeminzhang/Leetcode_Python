# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 23:24:15 2016

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
        m,n = len(matrix), len(matrix[0])
        if m==0 or n == 0: return False
        if target < matrix[0][0]: return False
        if target > matrix[m-1][n-1]: return False
        
        row = -1
        for i in range(m-1):
            if matrix[i][0] <= target and target < matrix[i+1][0]:
                row = i
                break
        if row == -1: row = m-1
        
        lis = matrix[row]
        length = len(lis)
        left = 0
        right = length-1
        mid = (left+right)/2
        while left <= right:
            if lis[mid] == target: return True
            elif lis[mid]> target:
                right = mid-1
                mid = (left+right)/2
            elif lis[mid] < target:
                left = mid+1
                mid = (left+right)/2
        return False