# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 09:52:58 2016

152. Maximum Product Subarray My Submissions Question

Total Accepted: 51390 Total Submissions: 239770 Difficulty: Medium
Find the contiguous subarray within an array (containing at least one number)
 which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.

****这里的连续指的是index连续 而不是里面的值

解题思路：主要需要考虑负负得正这种情况，比如之前的最小值是一个负数，再乘以一个负数就有可能成为一个很大的正数。
@author: zeminzhang
"""

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_min, num_max, num = nums[0], nums[0], nums[0]
        res = nums[0]
        for i in range(1,len(nums)):
            a = nums[i]*num_min
            b = nums[i]*num_max
            c = nums[i]
            
            num_min = min(a,b,c)
            num_max = max(a,b,c)
            res = max(res,num_max)
        return res
        