# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 07:44:53 2016

90. Subsets II

Total Accepted: 58969 Total Submissions: 199473 Difficulty: Medium

Given a collection of integers that might contain duplicates, nums, return all possible subsets.

Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
For example,
If nums = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]

还是那个dfs， 一定要掌握好！！

@author: zeminzhang
"""

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(depth, start, valuelist):
            if valuelist not in res:
                res.append(valuelist)
            if depth == len(nums): return
            for i in range(start, len(nums)):
                dfs(depth+1, i+1, valuelist+[nums[i]])
        nums.sort()
        res = []
        dfs(0, 0, [])
        return res