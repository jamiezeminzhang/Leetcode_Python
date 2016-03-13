# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 11:52:31 2016

You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?


先将矩阵转置，然后将矩阵的每一行翻转，就可以得到所要求的矩阵了。

@author: zeminzhang
"""

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        
        n = len(matrix)
        if n == 0: return []
        
        for i in range(n):
            for j in range(i+1,n):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = tmp
        
        for i in range(n):
            for j in range(n/2):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[i][n-1-j]
                matrix[i][n-1-j] = tmp

