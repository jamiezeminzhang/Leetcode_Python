# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 13:43:21 2016

268. Missing Number My Submissions Question

Total Accepted: 39162 Total Submissions: 100071 Difficulty: Medium
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing 
from the array.

For example,
Given nums = [0, 1, 3] return 2.

Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant 
extra space complexity?
Another great solution using XOR

class Solution(object):
    def missingNumber(self, nums):
        a = reduce(operator.xor, nums)
        b = reduce(operator.xor, range(len(nums) + 1))
        return a ^ b

@author: Jamie
"""

class Solution(object):
    def missingNumber(self, nums):
        return (1+len(nums))*len(nums)/2 - sum(nums)