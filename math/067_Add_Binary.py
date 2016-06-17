# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 03:46:59 2016

67. Add Binary

Total Accepted: 88158 Total Submissions: 315793 Difficulty: Easy

Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".

@author: zeminzhang
"""

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a, b = a[::-1], b[::-1]
        if len(a)>len(b):
            a, b = b,a 
        
        carry, i, res = 0, 0, ''
        while i<len(b):
            tmp = int(b[i])+carry if i>=len(a) else int(a[i])+int(b[i])+carry
            if tmp == 0:res += '0'
            elif tmp == 1:
                res += '1'
                carry = 0
            elif tmp == 2:
                res += '0'
                carry = 1
            else:
                res += '1'
                carry = 1
            i += 1
        return res[::-1] if carry == 0 else '1'+res[::-1] 
