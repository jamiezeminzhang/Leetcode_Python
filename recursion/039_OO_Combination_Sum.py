# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 21:30:54 2016

39. Combination Sum   

Total Accepted: 89892 Total Submissions: 290560 Difficulty: Medium

Given a set of candidate numbers (C) and a target number (T), find all unique 
combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order. 
(ie, a1 ≤ a2 ≤ … ≤ ak).
The solution set must not contain duplicate combinations.
For example, given candidate set 2,3,6,7 and target 7, 
A solution set is: 
[7] 
[2, 2, 3] 


解题思路：穷举出符合条件的组合，我们一般考虑dfs。

@author: zeminzhang
"""

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def dfs(start, target, valuelist):
            if target == 0: 
                res.append(valuelist)
                return
            for i in range(start, len(candidates)):
                if candidates[i] > target: return
                dfs(i, target-candidates[i], valuelist+[candidates[i]])
                
        candidates.sort()
        res = []
        dfs(0, target, [])
        return res
        
        
        