# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 14:53:32 2015

LeetCode # 26 Remove Duplicates from Sorted Array

 Given a sorted array, remove the duplicates in place such that each element 
 appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with 
constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums
 being 1 and 2 respectively. It doesn't matter what you leave beyond the new length. 

@author: zzhang
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        for num in nums:
            if i==0 or num > nums[i-1]:
                nums[i] = num
                i+=1
        return i
sol = Solution()
print sol.removeDuplicates([1,1,2,3,4,4,5])