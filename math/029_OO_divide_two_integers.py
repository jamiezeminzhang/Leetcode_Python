# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 13:26:20 2015

LeetCode #29: Divide Two Integers

Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT. 


@author: zzhang
"""

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        MAX_INT = 2**31-1
        negative = (dividend>0)^(divisor>0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                res += i
                i += i
                temp += temp
        
        if negative: res = 0-res
        return min(max(-MAX_INT-1,res),MAX_INT)