# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 05:33:03 2016

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
        center = (left+right)/2
        while left <= right:
            if center**2 == x:
                return center
            elif center**2 >x:
                right = center-1
                center = (left+right)/2
            else:
                left = center+1
                center = (left+right)/2
        return right