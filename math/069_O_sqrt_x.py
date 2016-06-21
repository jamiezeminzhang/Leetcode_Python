# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 05:33:03 2016

69. Sqrt(x)

Total Accepted: 98280 Total Submissions: 383389 Difficulty: Medium

Implement int sqrt(int x).

Compute and return the square root of x.

@author: zeminzhang
"""

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0: return 0
        left, right = 0, x
        while left<=right:
            mid = (left+right)/2
            if x>mid**2:
                left = mid+1
            elif x<mid**2:
                right = mid-1
            else:
                return mid
        return right