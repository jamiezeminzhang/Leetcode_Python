# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 02:17:44 2016

53. Maximum Subarray

Total Accepted: 114866 Total Submissions: 311573 Difficulty: Medium

Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [−2,1,−3,4,−1,2,1,−5,4],
the contiguous subarray [4,−1,2,1] has the largest sum = 6.


@author: zeminzhang
"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """ 
        max_sum, this_sum = -abs(nums[0]), 0
        for num in nums:
            if this_sum<0: this_sum = 0 #如果之前比0小，直接放弃选下一个，无论都大都比加之前的大
            this_sum += num
            max_sum = max(max_sum, this_sum)
        return max_sum