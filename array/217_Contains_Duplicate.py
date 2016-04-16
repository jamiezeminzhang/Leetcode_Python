# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 17:54:51 2016

217. Contains Duplicate
Total Accepted: 69800 Total Submissions: 173358 Difficulty: Easy

Given an array of integers, find if the array contains any duplicates. 
Your function should return true if any value appears at least twice in the array, 
and it should return false if every element is distinct.


一个非常漂亮的解法。。。。

class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums))
        
@author: Jamie
"""

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sp = set()
        for i in nums:
            if i in sp: return True
            else: sp.add(i)
        return False