# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 22:09:01 2016

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
    def DFS(self, candidates, target , start, val_list,sol):
        if target == 0:
            if val_list not in sol:
                return sol.append(val_list)
            else:
                return sol
        else:
            for i in range(start, len(candidates)):
                tmp = candidates[i]
                if tmp > target:
                    return
                self.DFS(candidates, target - tmp, i+1 , val_list+[tmp],sol)
        
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        sol = []
        self.DFS(candidates,target,0,[],sol)
        return sol

a = Solution()
print a.combinationSum2([10,1,2,7,6,1,5],8)