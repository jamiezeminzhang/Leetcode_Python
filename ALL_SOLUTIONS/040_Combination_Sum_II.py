# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 22:09:01 2016

40. Combination Sum II 

Total Accepted: 67636 Total Submissions: 245209 Difficulty: Medium

Given a collection of candidate numbers (C) and a target number (T), find all 
unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order. 
(ie, a1 ≤ a2 ≤ … ≤ ak).
The solution set must not contain duplicate combinations.
For example, given candidate set 10,1,2,7,6,1,5 and target 8, 
A solution set is: 
[1, 7] 
[1, 2, 5] 
[2, 6] 
[1, 1, 6] 

@author: zeminzhang
"""

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def dfs(start, target, valuelist):
            if target == 0:
                if valuelist not in res: res.append(valuelist)
                return
            for idx in range(start, len(candidates)):
                if target<candidates[idx]: return
                dfs(idx+1, target-candidates[idx], valuelist+[candidates[idx]])
                
        candidates.sort()
        res = []
        dfs(0, target, [])
        return res