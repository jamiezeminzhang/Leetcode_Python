# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 08:58:18 2016

80. Remove Duplicates from Sorted Array II My Submissions Question
Total Accepted: 64663 Total Submissions: 203097 Difficulty: Medium
Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums 
being 1, 1, 2, 2 and 3. It doesn't matter what you leave beyond the new length.

@author: zeminzhang
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        i,count = 0,0
        if length == 0 or length == 1 or length == 2:
            return length
            
        while i<=len(nums)-1:
            if i == 0 or i == 1:
                count += 1
                i += 1
            elif i >=2 and nums[i] != nums[i-1]:
                count += 1
                i += 1
            elif i >=2 and nums[i] == nums[i-1]:
                if nums[i-2] != nums[i-1]:
                    count += 1
                    i += 1
                else:
                    del nums[i]
        return count