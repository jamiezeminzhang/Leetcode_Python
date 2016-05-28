# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 10:59:58 2016

45. Jump Game II

Total Accepted: 63097 Total Submissions: 249855 Difficulty: Hard

Given an array of non-negative integers, you are initially positioned at the 
first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

For example:
Given array A = [2,3,1,1,4]

The minimum number of jumps to reach the last index is 2. (Jump 1 step from 
index 0 to 1, then 3 steps to the last index.)

Note:
You can assume that you can always reach the last index.


@author: zeminzhang
"""
# We use "last" to keep track of the maximum distance that has been reached
# by using the minimum steps "steps", whereas "curr" is the maximum distance
# that can be reached by using "steps+1" steps. Thus,curr = max(i+A[i]) where 0 <= i <= last.
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        steps, last, curr = 0, 0, 0
        for i in range(len(nums)):
            if i>last:
                last = curr
                steps += 1
            curr = max(curr, i+nums[i])
        return steps
                       
            
