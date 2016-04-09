# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 09:50:59 2016

219. Contains Duplicate II My Submissions Question

Total Accepted: 45981 Total Submissions: 157951 Difficulty: Easy
Given an array of integers and an integer k, find out whether there are two distinct indices 
i and j in the array such that nums[i] = nums[j] and the difference between i and j is at most k.

@author: Jamie
"""

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dic = {}
        for i in range(len(nums)):
            if not nums[i] in dic or i-dic[nums[i]]>k:
                dic[nums[i]] = i
            else:
                return True
        return False