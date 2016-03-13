# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 07:01:20 2016

191. Number of 1 Bits My Submissions Question

Total Accepted: 74814 Total Submissions: 198879 Difficulty: Easy
Write a function that takes an unsigned integer and returns the number of ’1' bits it has 
(also known as the Hamming weight).

For example, the 32-bit integer ’11' has binary representation 00000000000000000000000000001011, 
so the function should return 3.


@author: Jamie
"""

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        while n > 0:
            res += 1 if n%2 == 1 else 0
            n = n/2
        return res
        