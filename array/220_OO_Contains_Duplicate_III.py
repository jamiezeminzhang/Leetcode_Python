# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 10:18:01 2016

220. Contains Duplicate III

Total Accepted: 22741 Total Submissions: 125630 Difficulty: Medium

Given an array of integers, find out whether there are two distinct indices i and j in the array 
such that the difference between nums[i] and nums[j] is at most t and the difference between i and j is at most k.

The idea is like the bucket sort algorithm. Suppose we have consecutive buckets covering the range
 of nums with each bucket a width of (t+1). If there are two item with difference <= t, one of the two will happen:

(1) the two in the same bucket
(2) the two in neighbor buckets

每次同时最多有K个连续数字在t+1个bucket里
只要是在bucket里的数字满足条件就可以
但实际上只需要考虑左右两个bucket [-t-1,t+1] 这样的范围内就好

@author: Jamie
"""

class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if t<0: return False
        length = len(nums)
        d = {}
        t += 1
        for i in xrange(length):
            if i > k:
                del d[nums[i-k-1]/t]
            m = nums[i]/t
            if m in d:
                return True
            if m-1 in d and abs(nums[i]-d[m-1]) < t:
                return True
            if m+1 in d and abs(nums[i]-d[m+1]) < t:
                return True
            d[m] = nums[i]
        return False
        
        
sol = Solution()
print sol.containsNearbyAlmostDuplicate([2,4],1,1)