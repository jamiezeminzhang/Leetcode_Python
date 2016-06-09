# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 03:39:51 2016

62. Unique Paths

Total Accepted: 90528 Total Submissions: 246591 Difficulty: Medium

A robot is located at the top-left corner of a m x n grid (marked 'Start' in 
the diagram below).

The robot can only move either down or right at any point in time. The robot is 
trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

@author: zeminzhang
"""

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m==0 or n==0:
            return 0
        if m == 1 or n == 1:
            return 1
        
        a = m + n -2
        b = m - 1
        num1, num2 = 1,1
        
        for i in range(b):
            num1 *= a
            a -= 1
        
        while b>0:
            num2 *= b
            b -= 1
        
        return num1/num2