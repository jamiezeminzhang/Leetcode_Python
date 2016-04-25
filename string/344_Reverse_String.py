# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 10:58:24 2016

344. Reverse String

Total Accepted: 5092 Total Submissions: 8517 Difficulty: Easy

Write a function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh".

@author: Jamie
"""

class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]