# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 17:22:00 2016

228. Summary Ranges

Total Accepted: 37795 Total Submissions: 163553 Difficulty: Easy

Given a sorted integer array without duplicates, return the summary of its ranges.

For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].

A shorter solution
class Solution:
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        x, size = 0, len(nums)
        ans = []
        while x < size:
            c, r = x, str(nums[x]) # c is the start of x
            while x + 1 < size and nums[x + 1] - nums[x] == 1:
                x += 1
            if x > c:
                r += "->" + str(nums[x])
            ans.append(r)
            x += 1
        return ans
        
@author: Jamie
"""

class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums: return []
        res, cur_str, cur_num = [], str(nums[0]), nums[0]
        for num in nums[1:]:
            if num == cur_num+1:
                cur_num = num
            else:
                if cur_num == int(cur_str):
                    res.append(cur_str)
                else:
                    res.append(cur_str+'->'+str(cur_num))
                cur_str, cur_num = str(num), num
        if int(cur_str) == cur_num: 
            res.append(cur_str)
        else: 
            res.append(cur_str+'->'+str(cur_num))
        return res
            
