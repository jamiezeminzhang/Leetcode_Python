# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 03:38:04 2016

66. Plus One

Total Accepted: 104513 Total Submissions: 305610 Difficulty: Easy

Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.

@author: zeminzhang
"""

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        length = len(digits)
        if length == 1:
            if digits[0]<=8:
                digits[0] += 1
                return digits
            else:
                digits[0] = 0
                digits.insert(0,1)
                return digits
        else:
            if digits[-1] <=8:
                digits[-1] += 1
                return digits
            else:
                return self.plusOne(digits[:-1])+[0]