# -*- coding: utf-8 -*-
"""
Created on Friday July 5 08:58:24 2016

367. Valid Perfect Square

Total Accepted: 5007
Total Submissions: 13844
Difficulty: Medium

Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Returns: True
Example 2:

Input: 14
Returns: False

@author: zzhang
"""

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num==0 or num==1: return True
        left, right = 0, num/2
        while left<=right:
            mid = (left+right)/2
            if mid**2==num: return True
            elif mid**2<num:
                left = mid+1
            else:
                right = mid-1
        return False