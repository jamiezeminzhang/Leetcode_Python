# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 14:32:27 2015

LeetCode #7 Reverse Integer

Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321 

@author: zzhang
"""
# Remember using 31 instead of 32!!!

class Solution:
    # @param {integer} x
    # @return {integer}
    def reverse(self, x):
        of = 31
        if x > 2**of-1:
            return 0
        elif x >=0:
            s = str(x)
            y = s[::-1]
            if abs(int(y)) <= 2**of-1:
                return int(y)
            else:
                return 0
        else:
            s = str(-1*x)
            y = s[::-1]
            if abs(int(y)) <= 2**of-1:
                return -1*int(y)
            else:
                return 0