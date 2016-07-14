# -*- coding: utf-8 -*-
"""
Created on Thursday July 14 07:07:11 2016

372. Super Pow  

Total Accepted: 2171
Total Submissions: 7216
Difficulty: Medium

Your task is to calculate ab mod 1337 where a is a positive integer and b is an extremely large positive integer given in the form of an array.

Example1:

a = 2
b = [3]

Result: 8
Example2:

a = 2
b = [1,0]

Result: 1024

@author: zzhang

"""

class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        res = 1
        for po in b:
            res = pow(res, 10, 1337) * pow(a, po, 1337) % 1337
        return res
