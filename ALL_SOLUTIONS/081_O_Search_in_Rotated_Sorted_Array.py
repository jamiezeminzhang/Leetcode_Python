# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 21:34:58 2016

81. Search in Rotated Sorted Array II My Submissions Question
Total Accepted: 55334 Total Submissions: 175185 Difficulty: Medium
Follow up for "Search in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?

Write a function to determine if a given target is in the array.

2分查找的变种。需要注意判断什么时候，哪边是顺序。无法判断的时候就left++ right--。

@author: zeminzhang
"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        length = len(nums)
        left, right = 0, length-1
        while left <= right:
            mid = (left+right)/2
            if nums[mid] == target: return True
            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1
            elif nums[mid] >= nums[left]: # left part increasing
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:# right part increasing
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False