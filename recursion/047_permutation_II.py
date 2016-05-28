# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 11:38:11 2016

47. Permutations II

Total Accepted: 71489 Total Submissions: 253924 Difficulty: Medium


Given a collection of numbers that might contain duplicates,
return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[1,1,2], [1,2,1], and [2,1,1].

@author: zeminzhang
"""
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0: return []
        if len(nums) == 1: return [nums]
        
        duplicate = set()
        res = []
        for i in range(len(nums)):
            if nums[i] not in duplicate:
                duplicate.add(nums[i])
            else:
                continue # 如果已经有这个元素就跳过
            for j in self.permuteUnique(nums[:i] + nums[i+1:]):
                res.append([nums[i]] + j) # num[i] 开头的所有组合都有了
        return res

sol = Solution()
print sol.permuteUnique([1,1,2])
