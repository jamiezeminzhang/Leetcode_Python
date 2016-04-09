# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 15:22:17 2015

LeetCode # 27 Remove Element

Given an array and a value, remove all instances of that value in place and return the new length.

The order of elements can be changed. It doesn't matter what you leave beyond the new length. 

@author: zzhang
"""

class Solution:
    # @param {integer[]} nums
    # @param {integer} val
    # @return {integer}
    def removeElement(self, nums, val):
        if len(nums) == 0:
            return 0
        l = len(nums)
        for idx,i in enumerate(nums):
            if i == val:
                l -= 1
        for i in range(len(nums)-l):
            nums.remove(val)
        return l

sol = Solution()
print sol.removeElement([3,3,3,3],4)