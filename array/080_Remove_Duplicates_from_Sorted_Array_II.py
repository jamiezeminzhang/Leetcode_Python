# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 08:58:18 2016

80. Remove Duplicates from Sorted Array

Total Accepted: 64663 Total Submissions: 203097 Difficulty: Medium

Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums 
being 1, 1, 2, 2 and 3. It doesn't matter what you leave beyond the new length.

*** Pochman's answer ***
令i为输出nums的结尾。如果每次循环的数字大于nums[i-2]，那么就令nums[i]=n, i++
	
@author: zeminzhang
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        for n in nums:
            if i<2 or n>nums[i-2]:
                nums[i]=n
                i+=1
        return i