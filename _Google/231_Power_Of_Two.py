# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 09:28:47 2016

231. Power of Two

Total Accepted: 94575
Total Submissions: 247044
Difficulty: Easy

Given an integer, write a function to determine if it is a power of two.

Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.

Some good solutions:

return n>0 and (bin(n).count('1') == 1)

return n>0 and n&(n-1) == 0 
And of nearby numbers will only be 0 when is like 10000 and 1111 

@author: Jamie
"""

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return str(bin(n)[2:]) == '1'+(len(bin(n))-3)*'0'
        