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

Note:
Your solution should be in logarithmic complexity.

Credits:
Special thanks to @ts for adding this problem and creating all test cases.


*** This problem is equivalent to finding a local maximum via binary search***

@author: Jamie
"""

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.helper(nums,0,len(nums)-1)
        
    def helper(self, nums, left, right):
        if left==right: return left
        mid1 = (left+right)/2; mid2 = mid1+1
        if nums[mid1]>nums[mid2]: return self.helper(nums,left, mid1)
        else: return self.helper(nums,mid2,right)
        
        