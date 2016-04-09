# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 10:28:36 2016

153. Find Minimum in Rotated Sorted Array

Total Accepted: 79047 Total Submissions: 223528 Difficulty: Medium

Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.

@author: zeminzhang
"""

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<=1: return nums[0]
        left, right = 0, len(nums)-1
        while left<right:
            mid = (left+right)/2
            if nums[mid]>nums[right]:left = mid+1
            else:right = mid
        return nums[right]