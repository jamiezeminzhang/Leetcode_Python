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

class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if len(A) == 0:
            return 0
        j = 0
        for i in range(0, len(A)):
            if A[i] != A[j]:
                A[i], A[j+1] = A[j+1], A[i]
                j = j + 1
        return j+1

		

@author: zzhang
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <=1: return len(nums)
        
        left = 0
        for i in range(1,len(nums)):
            if nums[left] == nums[i]:
                continue
            else:
                left += 1
                nums[left] = nums[i]
        return left+1

sol = Solution()
print sol.removeDuplicates([1,1,2,3,4,4,5])