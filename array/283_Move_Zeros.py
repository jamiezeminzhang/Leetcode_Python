# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 14:16:35 2016

283. Move Zeroes

Total Accepted: 57202 Total Submissions: 131765 Difficulty: Easy

Given an array nums, write a function to move all 0's to the end of it while maintaining the 
relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.

@author: Jamie
"""

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        i,k = 0,0
        while i < length-k:
            if nums[i] == 0:
                nums.remove(0)
                nums.append(0)
                k += 1
            else:
                i+=1
                