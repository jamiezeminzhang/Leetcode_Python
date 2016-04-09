# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 06:26:38 2016

189. Rotate Array My Submissions Question

Total Accepted: 61027 Total Submissions: 299673 Difficulty: Easy
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.

[show hint]

Hint:
Could you do it in-place with O(1) extra space?
Related problem: Reverse Words in a String II

@author: Jamie
"""

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            tmp = nums.pop()
            nums.insert(0,tmp)
        