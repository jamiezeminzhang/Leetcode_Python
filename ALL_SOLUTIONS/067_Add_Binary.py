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
        a = a[::-1]
        b = b[::-1]
        if len(a) > len(b):  # make len(a) <= len(b)
            tmp = a
            a = b
            b = tmp

        carry = 0
        i = 0
        c = ""
        while i < len(a):
            if a[i] == '0' and b[i] == '0': 
                c += '0' if carry == 0 else '1'
                carry = 0
            if ( a[i] == '1' and b[i] == '0' ) or ( a[i] == '0' and b[i] == '1' ):
                if carry == 0:
                    c += '1'
                else:
                    c += '0'
            if a[i] == '1' and b[i] == '1':
                if carry == 0:
                    c += '0'
                    carry = 1
                else:
                    c += '1'
            i += 1
        
        while i < len(b):
            print i
            if carry == 0:
                c += b[i]
            else:
                if b[i] == '0':
                    c += '1'
                    carry = 0
                else:
                    c += '0'
            i += 1
        if i == len(b) and carry == 1:
            c += '1'
        c = c[::-1]
        return c
        
sol = Solution()
print sol.addBinary('1','1')