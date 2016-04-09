# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 02:31:32 2016

88. Merge Sorted Array My Submissions Question
Total Accepted: 85762 Total Submissions: 288821 Difficulty: Easy
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as 
one sorted array.

Note:
You may assume that nums1 has enough space (size that is greater or equal to 
m + n) to hold additional elements from nums2. The number of elements 
initialized in nums1 and nums2 are m and n respectively.

My solution:
compare + insert + compare + insert...

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        while m>0 and n>0:
            if nums1[m-1]>nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m-=1
            else:
                nums1[m+n-1] = nums2[n-1]
                n-=1
        if n>0:
            nums1[:n] = nums2[:n]

@author: zeminzhang
"""

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        if m == 0: 
            for i in range(n):
                nums1[i] = nums2[i]
            return
        if n == 0: return
        start = 0
        for i in range(n):
            while start <= i+m-1 and nums2[i] >= nums1[start]:
                start += 1
            nums1.insert(start,nums2[i])
            if start == i+m:
                nums1[i+m+1:] = nums2[i+1:]
                break
        del nums1[m+n:]
        
sol = Solution()
a = [1,2,3,0,0,0]
b = [4,5,6]
sol.merge(a,3,b,3)
print a