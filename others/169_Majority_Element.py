# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 09:39:13 2016

169. Majority Element

Total Accepted: 93017 Total Submissions: 233808 Difficulty: Easy

Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

*** Remember how to return the key with the max value of a dictionary

max(dic, key=lambda i: dic[i])

*** Another solution with O(n) time and O(1) space ***
** Majority Vote ***

class Solution(object):
    def majorityElement(self, nums):
        major, count = nums[0], 1
        for i in range(1,len(nums)):
            if count == 0: major = nums[i]; count += 1
            elif nums[i] == major: count += 1
            else: count -= 1
        return major
		
***
@author: Jamie
"""

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        dic = {}
        for num in nums:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1
        
        return max(dic, key=lambda i: dic[i])