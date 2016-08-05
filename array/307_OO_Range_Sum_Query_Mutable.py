# -*- coding: utf-8 -*-
"""
307. Range Sum Query - Mutable

Total Accepted: 16020
Total Submissions: 87320
Difficulty: Medium

Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

The update(i, val) function modifies nums by updating the element at index i to val.
Example:
Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8
Note:
The array is only modifiable by the update function.
You may assume the number of calls to update and sumRange function is distributed evenly.

@author: zzhang
"""

class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.nums = nums
        self.sums = [0]*(len(nums)+1)
        self.n = len(nums)
        for i in range(self.n):
            self.add(i+1,nums[i])
        
    def add(self, i, val):
        while i <= self.n:
            self.sums[i] += val
            i += self.lowbit(i)
    
    def lowbit(self, x):
        return x&-x

    def sum(self, i):
        res = 0
        while i>0:
            res += self.sums[i]
            i -= self.lowbit(i)
        return res
        
    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        self.add(i+1, val-self.nums[i])
        self.nums[i] = val

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        if not self.nums: return 0
        else: return self.sum(j+1) - self.sum(i)


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.update(1, 10)
# numArray.sumRange(1, 2)
