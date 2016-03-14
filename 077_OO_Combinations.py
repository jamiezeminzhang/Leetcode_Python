# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 05:40:46 2016

77. Combinations My Submissions Question
Total Accepted: 65422 Total Submissions: 198083 Difficulty: Medium
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

@author: zeminzhang
"""

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def dfs(start, valuelist):
            if len(valuelist)==k: 
                res.append(valuelist)
                return
            for i in range(start,n+1):
                dfs(i+1, valuelist+[i])
        res = []
        dfs(1,[])
        return res