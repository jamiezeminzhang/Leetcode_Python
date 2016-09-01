# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 20:29:25 2016

54. Spiral Matrix

Total Accepted: 61157 Total Submissions: 268316 Difficulty: Medium

Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].

@author: zeminzhang
"""

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix: return []
        res = matrix.pop(0)
        matrix = [list(x) for x in zip(*matrix)[::-1]]
        return res + self.spiralOrder(matrix)     
        