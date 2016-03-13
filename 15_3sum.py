# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 09:53:41 2015

LeetCode #15 3Sum

Given an array S of n integers, are there elements a, b, c in S such that 
a + b + c = 0? 
Find all unique triplets in the array which gives the sum of zero.

Note:

    Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
    The solution set must not contain duplicate triplets.

    For example, given array S = {-1 0 1 2 -1 -4},

    A solution set is:
    (-1, 0, 1)
    (-1, -1, 2)


@author: zzhang
"""
class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def threeSum(self, nums): 
        
        if len(nums)<=2:
            return []
            
        res =  []
        d = {}
        for idx,i in enumerate(nums):
            if i not in d:
                d[i] = 1
                nums_wo_i = list(nums)
                nums_wo_i.remove(i)
                res_temp = self.TwoSum(nums_wo_i,-1*i)
                if len(res_temp) != 0:
                    for j in range(len(res_temp)):
                        res_temp[j].append(i)
                        res_temp[j].sort()
                    for k in res_temp:
                        if k not in res:
                            res.append(k)
        return res
            
    def TwoSum(self,num,target):
        d = {}
        result = []
        for idx,i in enumerate(num):
            if target - i not in d:
                d[i] = idx
            else:
                result.append([i,target-i])
        return result

sol = Solution()
print sol.threeSum([-7,-11,12,-15,14,4,4,11,-11,2,-8,5,8,14,0,3,2,3,-3,-15,-2,3,6,1,2,8,-5,-7,3,1,8,11,-3,6,3,-4,-13,-15,14,-8,2,-8,4,-13,13,11,5,0,0,9,-8,5,-2,14,-9,-15,-1,-6,-15,9,10,9,-2,-8,-8,-14,-5,-14,-14,-6,-15,-5,-7,5,-11,14,-7,2,-9,0,-4,-1,-9,9,-10,-11,1,-4,-2,2,-9,-15,-12,-4,-8,-5,-11,-6,-4,-9,-4,-3,-7,4,9,-2,-5,-13,7,2,-5,-12,-14,1,13,-9,-3,-9,2,3,8,0,3])