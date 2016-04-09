# -*- coding: utf-8 -*-
"""
Created on Tue Aug 04 13:08:49 2015

LeetCode # 35: Search Insert Position

Given a sorted array and a target value, return the index if the target is 
found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0 

@author: zzhang
"""

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lenNum = len(nums)
        left, right = 0, lenNum-1
        
        while left<=right:
            mid = (left+right)/2
            if target == nums[mid]: return mid
            elif nums[left]<=target<nums[mid]:
                right = mid-1
            elif nums[mid]<target<=nums[right]:
                left = mid+1
            elif target<nums[left]:
                return left
            elif target>nums[right]:
                return right+1
        
sol = Solution()
print sol.searchInsert([1,3],3)