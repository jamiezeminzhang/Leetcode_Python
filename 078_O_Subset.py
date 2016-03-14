# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 07:53:05 2016

78. Subsets My Submissions Question
Total Accepted: 81525 Total Submissions: 269896 Difficulty: Medium
Given a set of distinct integers, nums, return all possible subsets.

Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
For example,
If nums = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

解题思路：碰到这种问题，一律dfs。

class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    
    def subsets(self, S):
        def dfs(depth, start, valuelist):
            res.append(valuelist)
            if depth == len(S): return
            for i in range(start, len(S)):
                dfs(depth+1, i+1, valuelist+[S[i]])
        S.sort()
        res = []
        dfs(0, 0, [])
        return res
		
下面的答案给的是直接法
@author: zeminzhang
"""

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for num in sorted(nums):
            res += [item+[num] for item in res]
        return res
        
sol = Solution()
print sol.subsets([1,2,3])
        