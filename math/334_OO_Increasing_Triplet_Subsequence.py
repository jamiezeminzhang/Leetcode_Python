# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 11:37:27 2016

334. Increasing Triplet Subsequence

Total Accepted: 4767 Total Submissions: 14607 Difficulty: Medium

Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

Formally the function should:
Return true if there exists i, j, k 
such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
Your algorithm should run in O(n) time complexity and O(1) space complexity.

Examples:
Given [1, 2, 3, 4, 5],
return true.

Given [5, 4, 3, 2, 1],
return false.

@author: Jamie
"""

class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        a, b = None, None
        for n in nums:
            if a == None or a>=n:
                a = n
            elif b == None or b>=n:
                b = n
            else: 
                return True
        return False