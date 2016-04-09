# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 06:27:26 2016

190. Reverse Bits My Submissions Question

Total Accepted: 52680 Total Submissions: 180895 Difficulty: Easy
Reverse bits of a given 32 bits unsigned integer.

For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), return 964176192 (represented in binary as 00111001011110000010100101000000).

Follow up:
If this function is called many times, how would you optimize it?

Related problem: Reverse Integer

@author: Jamie
"""

class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = bin(n)[2:]; length = len(s)
        if length<32: s = '0'*(32-length) + s
        s = s[::-1]
        return int(s,2)