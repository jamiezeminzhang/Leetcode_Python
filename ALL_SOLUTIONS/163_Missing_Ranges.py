# -*- coding: utf-8 -*-
"""
Created on Friday Aug 5 9:13:41 2016

163. Missing Ranges

Total Accepted: 13666
Total Submissions: 45314
Difficulty: Medium

Given a sorted integer array where the range of elements are [lower, upper] inclusive, return its missing ranges.

For example, given [0, 1, 3, 50, 75], lower = 0 and upper = 99, return ["2", "4->49", "51->74", "76->99"].

@author: zzhang


"""

class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        if not nums:
            if lower == upper: return [str(lower)]
            else: return [str(lower)+'->'+str(upper)]
        nums = [lower-1] + nums + [upper+1]
        res, cur = [], 's'
        for num in nums:
            if cur == 's':
                cur = num
            else:
                if num-cur>2:
                    res.append(str(cur+1) + '->' + str(num-1))
                elif num-cur==2:
                    res.append(str(num-1))
                cur = num
        return res
                
            
