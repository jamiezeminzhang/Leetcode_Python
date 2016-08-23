# -*- coding: utf-8 -*-
"""
2016/08/11 08:56 PST

280. Wiggle Sort  

Total Accepted: 14223
Total Submissions: 27501
Difficulty: Medium

Given an unsorted array nums, reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]....

For example, given nums = [3, 5, 2, 1, 6, 4], one possible answer is [1, 6, 2, 5, 3, 4].

＊＊奇数index应该大，偶数index应该小

class Solution(object):
    def wiggleSort(self, nums):
        for i in range(1, len(nums)):
            if (i%2==1 and nums[i]<nums[i-1]) or (i%2==0 and nums[i]>nums[i-1]):
                nums[i-1], nums[i] = nums[i], nums[i-1]

"""

class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums)<=1: return
        
        index = 1
        while index<len(nums):
            if index < len(nums)-1:
                if nums[index] < max(nums[index-1], nums[index+1]):
                    if nums[index-1]>nums[index+1]:
                        nums[index-1], nums[index] = nums[index], nums[index-1]
                    else:
                        nums[index+1], nums[index] = nums[index], nums[index+1]
            else:
                if nums[index]<nums[index-1]:
                    nums[index-1], nums[index] = nums[index], nums[index-1]
            index += 2