# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 11:06:39 2015

LeetCode # 16 3Sum Closest

Given an array S of n integers, find three integers in S such that the sum 
is closest to a given number, target. Return the sum of the three integers. 
You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).


@author: zzhang
"""

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def threeSumClosest(self, nums, target):
        nums.sort()
        dif = 2**31-1
        res = 0
        
        for i in range(len(nums)):
            left = i + 1
            right = len(nums)-1
            while left<right:
                s = nums[i]+nums[left]+nums[right]
                dif_new = abs(s-target)
                if dif_new == 0: return s
                if s> target:right -= 1
                if s < target:left += 1
                if dif_new < dif:
                    dif = dif_new
                    res = s
        return res

sol = Solution()
print sol.threeSumClosest([1,2,3,4,5,6],2)