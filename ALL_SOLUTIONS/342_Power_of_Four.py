# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 16:17:13 2016

342. Power of Four

Total Accepted: 3328 Total Submissions: 9711 Difficulty: Easy

Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example:
Given num = 16, return true. Given num = 5, return false.

Follow up: Could you solve it without loops/recursion?

Credits:
Special thanks to @yukuairoy for adding this problem and creating all test cases.

Subscribe to see which companies asked this question

@author: Jamie
"""

class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return bin(num)[3:] == len(bin(num)[3:])*'0' and len(bin(num)[3:])%2==0 if num!=0 else False