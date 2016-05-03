# -*- coding: utf-8 -*-
"""
Created on Mon May 02 20:39:52 2016

347. Top K Frequent Elements

Total Accepted: 1132 Total Submissions: 2536 Difficulty: Medium
Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].

Note: 
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

@author: Jamie
"""

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = collections.Counter(nums)
        return sorted(count, key = count.get, reverse = True)[:k]