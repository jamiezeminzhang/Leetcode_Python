# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 07:04:37 2016

198. House Robber My Submissions Question

Total Accepted: 54202 Total Submissions: 163657 Difficulty: Easy
You are a professional robber planning to rob houses along a street. 
Each house has a certain amount of money stashed, the only constraint
 stopping you from robbing each of them is that adjacent houses have
 security system connected and it will automatically contact the police 
 if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money 
of each house, determine the maximum amount of money you can rob tonight without alerting the police.

@author: Jamie
"""

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length == 0: return 0
        if length == 1: return nums[0]
        if length == 2: return max(nums)
        dp = [0 for x in range(length)]
        dp[0] = nums[0]
        dp[1] = max(nums[:2])
        for i in range(2,length):
            dp[i] = max(dp[i-1],dp[i-2]+nums[i])
        
        return dp[length-1]