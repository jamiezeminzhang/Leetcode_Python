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
        length = len(nums)
        if length == 0: return []
        if length == 1: return [str(nums[0])]
        start, end = nums[0], 0
        res = []
        for i in xrange(1,length):
            if nums[i] != nums[i-1]+1:
                end = nums[i-1]
                if start == end:
                    res.append(str(start))
                else:
                    res.append(str(start)+'->'+str(end))
                start = nums[i]
            elif i == length-1:
                end = nums[i]
                if start == end:
                    res.append(str(start))
                else:
                    res.append(str(start)+'->'+str(end))
        if start>end:
            end = nums[-1]
            if start == end:
                res.append(str(start))
            else:
                res.append(str(start)+'->'+str(end))
        return res
            