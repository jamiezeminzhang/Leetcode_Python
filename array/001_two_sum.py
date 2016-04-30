# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 13:48:57 2015

LeetCode #1 Two Sum

Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, 
where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2 

@author: zzhang
"""

class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        d = {}
        for i, e in enumerate(num):
            if e in d:
                return d[e] + 1, i + 1
            d[target - e] = i
            

sol = Solution()
print sol.twoSum([2,5,3,7], 10)

a = {}
a[2] = 3