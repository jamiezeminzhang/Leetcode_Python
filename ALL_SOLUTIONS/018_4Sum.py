# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 13:46:15 2015

LeetCode # 18 4Sum

Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

    Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a ≤ b ≤ c ≤ d)
    The solution set must not contain duplicate quadruplets.

    For example, given array S = {1 0 -1 0 -2 2}, and target = 0.

    A solution set is:
    (-1,  0, 0, 1)
    (-2, -1, 1, 2)
    (-2,  0, 0, 2)


@author: zzhang
"""

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[][]}
    def fourSum(self, nums, target):
        numLen, res, dict  = len(nums), set(), {}
        if numLen <4:
            return []
        for i in range(0,numLen-1):
            for j in range(i+1,numLen):
                if (nums[i]+nums[j]) not in dict:
                    dict[nums[i]+nums[j]] = [(i,j)]
                else:
                    dict[nums[i]+nums[j]].append((i,j))
                
        for i in range(0,numLen-1):
            for j in range(i+1,numLen):
                T = target - nums[i] - nums[j]
                if T in dict:
                    for k in range(len(dict[T])):
                        if dict[T][k][0]!=i and dict[T][k][0] !=j \
                        and dict[T][k][1]!=i and dict[T][k][1]!=j:
                            temp = [nums[i],nums[j],nums[dict[T][k][0]],nums[dict[T][k][1]]]
                            temp.sort()
                            res.add((temp[0],temp[1],temp[2],temp[3]))
        return [list(i) for i in res]

sol = Solution();
print sol.fourSum([-3,-2,-1,0,0,1,2,3], 0)