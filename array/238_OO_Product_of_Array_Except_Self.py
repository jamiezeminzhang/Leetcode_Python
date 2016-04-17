# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 14:14:46 2016

238. Product of Array Except Self 

Total Accepted: 34611 Total Submissions: 83650 Difficulty: Medium

Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal 
to the product of all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].

Follow up:
Could you solve it with constant space complexity? (Note: The output array does not count as extra 
space for the purpose of space complexity analysis.)

**************** O(n) space *******************
one vector to track the product before i
one vector to track the produet after i


**************** O(1) space *******************
ditch the second vector and use a constant c going backwards

class Solution(object):
    def productExceptSelf(self, nums):
        if not nums: return []
        length = len(nums)
        ans = [1]
        for i in xrange(1,length):
            ans += ans[i-1]*nums[i-1],
        c = 1
        for i in xrange(length-1,-1,-1):
            ans[i] *=c
            c *= nums[i]
        return ans
        

@author: Jamie
"""

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums: return []
        length = len(nums)
        lis1 = [1]; lis2 = [1]*length
        for i in xrange(1,length):
            lis1 += lis1[i-1]*nums[i-1],
        for j in xrange(length-2,-1,-1):
            lis2[j] =  lis2[j+1]*nums[j+1] 
        ans = [0]*length
        for i in xrange(length):
            ans[i] = lis1[i]*lis2[i]
        return ans