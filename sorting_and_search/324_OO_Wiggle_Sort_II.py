# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 13:16:55 2016

324. Wiggle Sort II

Total Accepted: 5363 Total Submissions: 25223 Difficulty: Medium

Given an unsorted array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....

Example:
(1) Given nums = [1, 5, 1, 1, 6, 4], one possible answer is [1, 4, 1, 5, 1, 6]. 
(2) Given nums = [1, 3, 2, 2, 3, 1], one possible answer is [2, 3, 1, 3, 1, 2].

Note:
You may assume all input has valid answer.

Follow Up:
Can you do it in O(n) time and/or in-place with O(1) extra space?

*** Given answer is O(nlogn) time and O(n) space ***

*** Here is a O(n) time and O(1) space solution ***
Written by myself!!!
Fking 2 hours

class Solution(object):
    # partition in place within indices [left, right] inclusive
    # change num in place into [...numbers<num[idx]...,numbers==num[idx]...,...numbers>num[idx]... ]
    # return the idx after partition
    def partition(self, num, left, right, idx):
        num[idx], num[right] = num[right], num[idx]
        r1,r2 = right, right
        while left<r1:
            if num[left]<num[r1]:
                left += 1
            elif num[left] == num[r1]:
                num[left], num[r1-1] = num[r1-1], num[left]
                r1 -= 1
            elif num[left]>num[r1]:
                num[left], num[r1-1] = num[r1-1], num[left]
                num[r2], num[r1-1] = num[r1-1], num[r2]
                r1 -= 1
                r2 -= 1
        return r1
    
    # again, in place, put kth largest in mid
    def findkth(self, num, k):
        left, right = 0, len(num)-1
        while left<right:
            pivot = (left + right)/2
            idx = self.partition(num, left, right, pivot)
            if num[idx] == num[k]: break
            if idx>k:
                right = idx-1
            else:
                left = idx+1

    def wiggleSort(self, nums):
        mid = len(nums)/2
        self.findkth(nums, mid)       # find median and do partition
        if len(nums)%2 == 0:
            nums[::2], nums[1::2] = nums[:mid][::-1], nums[mid:][::-1]
        else:
            nums[::2], nums[1::2] = nums[:mid+1][::-1], nums[mid+1:][::-1]
        
        
        
@author: Jamie
"""

class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        snums = sorted(nums)
        for i in range(1,len(snums),2)+range(0,len(snums),2):
            nums[i] = snums.pop()
            