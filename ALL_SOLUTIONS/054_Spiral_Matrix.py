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
        if len(matrix) == 0: return []
        
        def dfs(matrix, val_list):        
            val_list += matrix[0]        
            if len(matrix) ==1: return val_list  
            
            del matrix[0]
            m = len(matrix)
            n = len(matrix[0])
            
            # rotate in counterclockwise
            b = [[0 for x in range(m)] for y in range(n)]
            for i in range(m):
                for j in range(n):
                    b[j][i] = matrix[i][j]
            b.reverse()
            return dfs(b, val_list)
        
        val_list = []
        dfs(matrix,val_list)
        return val_list

sol = Solution()
print sol.spiralOrder([[1,2,3],[4,5,6],[7,8,9]])        
        