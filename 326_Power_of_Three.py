# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 16:32:08 2016

326. Power of Three My Submissions Question
Total Accepted: 22291 Total Submissions: 62597 Difficulty: Easy
Given an integer, write a function to determine if it is a power of three.

Follow up:
Could you do it without using any loop / recursion?

class Solution(object):
    def isPowerOfThree(self, n):
        if n<=0: return False
        return 1162261467 % n == 0
        
@author: Jamie
"""



class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n>0 and 3**(round(math.log(n,3))) == n