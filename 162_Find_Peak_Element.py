# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 05:00:35 2016

162. Find Peak Element My Submissions Question

Total Accepted: 55900 Total Submissions: 170868 Difficulty: Medium
A peak element is an element that is greater than its neighbors.

Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that num[-1] = num[n] = -∞.

For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.

click to show spoilers.

Credits:
Special thanks to @ts for adding this problem and creating all test cases.

@author: Jamie
"""

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length == 1: return 0
        if length == 2: 
            if nums[0]< nums[1]: return 1
            if nums[0]> nums[1]: return 0

        i = 0
        while i< length:
            if i == 0: 
                if nums[i]>nums[i+1]: return i
            elif i == length-1:
                if nums[i]>nums[i-1]: return i
            elif nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                return i
            i+= 1
        
        