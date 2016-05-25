# -*- coding: utf-8 -*-
"""
Created on Wed May 25 11:35:12 2016

350. Intersection of Two Arrays II

Total Accepted: 4500 Total Submissions: 10780 Difficulty: Easy

Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

Note:
Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.

Follow up:
What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to num2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

@author: zeminzhang
"""

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        n1 = nums1 if len(nums1)<len(nums2) else nums2
        n2 = nums1 if len(nums1)>=len(nums2) else nums2
        
        s, res = collections.Counter(n2), []
        for i in n1:
            if s[i]>0: 
                res.append(i)
                s[i]-=1
        return res