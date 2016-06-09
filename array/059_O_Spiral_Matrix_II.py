# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 23:05:59 2016

59. Spiral Matrix II

Total Accepted: 54541 Total Submissions: 153968 Difficulty: Medium

Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

For example,
Given n = 3,

You should return the following matrix:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]


@author: zeminzhang
"""

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 0: return []
        if n == 1: return [[1]]
        
        res = [[0 for x in range(n)] for y in range(n)]
        up,down,left,right = 0,n-1,0,n-1
        direct =0
        count = 0
        
        while True:
            if direct == 0:
                for i in range(left,right+1):
                    count += 1
                    res[up][i] = count
                up+=1
                direct += 1
            if direct == 1:
                for i in range(up,down+1):
                    count+=1
                    res[i][right] = count
                right -= 1
                direct += 1
            if direct == 2:
                for i in range(right,left-1,-1):
                    count +=1
                    res[down][i] = count
                down -= 1
                direct += 1
            if direct == 3:
                for i in range(down, up-1, -1):
                    count += 1
                    res[i][left] = count
                left += 1
                direct += 1
            direct -= 4
            if count == n*n: return res
        