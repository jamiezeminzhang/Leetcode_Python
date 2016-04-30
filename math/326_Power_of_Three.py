# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 16:32:08 2016

326. Power of Three

Total Accepted: 22291 Total Submissions: 62597 Difficulty: Easy

Given an integer, write a function to determine if it is a power of three.

Follow up:
Could you do it without using any loop / recursion?

The positive divisors of 3**19 are exactly the powers of 3 from 3*0 to 3**19. 
That's all powers of 3 in the possible range here (signed 32-bit integer). 
So just check whether the number is positive and whether it divides 319.

@author: Jamie
"""



class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n>0 and 3**19%n==0