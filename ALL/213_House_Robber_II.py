# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 10:46:43 2016

213. House Robber II My Submissions Question

Total Accepted: 21978 Total Submissions: 74182 Difficulty: Medium
Note: This is an extension of House Robber.

After robbing those houses on that street, the thief has found himself a new place for his thievery 
so that he will not get too much attention. This time, all houses at this place are arranged in a 
circle. That means the first house is the neighbor of the last one. Meanwhile, the security system 
for these houses remain the same as for those in the previous street.

Given a list of non-negative integers representing the amount of money of each house, determine the
 maximum amount of money you can rob tonight without alerting the police.

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
        
        s = -1*sum(nums)
        nums1, nums2 = list(nums), list(nums)
        nums1[0] = s
        nums2[length-1] = s
        dp1 = [0 for x in range(length)]
        dp2 = [0 for x in range(length)]
        
        dp1[0] = nums1[0]; dp1[1] = max(nums1[:2])
        dp2[0] = nums2[0]; dp2[1] = max(nums2[:2])
        for i in range(2,length):
            dp1[i] = max( dp1[i-2]+nums1[i], dp1[i-1] , nums[i])
            dp2[i] = max( dp2[i-2]+nums2[i], dp2[i-1] , nums[i])

        return max(dp1[length-1], dp2[length-1])
        
        
sol = Solution()
print sol.rob([4,1,2])