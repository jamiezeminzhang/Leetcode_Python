# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 10:55:49 2016

Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

click to show follow up.

Follow up:
Did you use extra space?
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?

@author: zeminzhang
"""

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        
        m,n = len(matrix), len(matrix[0])
        row,col = [],[]
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row.append(i)
                    col.append(j)
        
        for i in row:
            for j in range(n):
                matrix[i][j] = 0
        for i in col:
            for j in range(m):
                matrix[j][i] = 0