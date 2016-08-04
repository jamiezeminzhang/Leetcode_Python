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
        i, carry = len(digits)-1, 1
        while i>=0:
            carry, digits[i] = (digits[i]+carry)/10, (digits[i]+carry)%10
            if carry == 0: break
            i -= 1
        if carry>0: digits.insert(0,1)
        return digits
