# -*- coding: utf-8 -*-
"""
Created on Tuesday Aug 23 09:11:20 2016

259. 3Sum Smaller

Given an array of n integers nums and a target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.

For example, given nums = [-2, 0, 1, 3], and target = 2.

Return 2. Because there are two triplets which sums are less than 2:

[-2, 0, 1]
[-2, 0, 3]
Follow up:
Could you solve it in O(n2) runtime?

Hide Company Tags Google
Hide Tags Array Two Pointers
Hide Similar Problems (M) 3Sum (M) 3Sum Closest

        
@author: Jamie
"""

class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        ans = 0
        while len(nums)>=3:
            cur_num = nums.pop()
            ans += self.twoSum(nums, target-cur_num)
        return ans
    
    def twoSum(self, nums, target):
        res = 0
        p1, p2 = 0, len(nums)-1
        while p1<p2:
            cur = nums[p1]+nums[p2]
            if cur<target:
                res += (p2-p1)
                p1 += 1
            else:
                p2-=1
        return res
                
                