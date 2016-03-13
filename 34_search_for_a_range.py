# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 17:39:22 2015

LeetCode # 34 Search for a Range

Given a sorted array of integers, find the starting and ending position 
of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4]. 

*** A cleaner solution
def searchRange(self, nums, target):
    def binarySearchLeft(A, x):
        left, right = 0, len(A) - 1
        while left <= right:
            mid = (left + right) / 2
            if x > A[mid]: left = mid + 1
            else: right = mid - 1
        return left

    def binarySearchRight(A, x):
        left, right = 0, len(A) - 1
        while left <= right:
            mid = (left + right) / 2
            if x >= A[mid]: left = mid + 1
            else: right = mid - 1
        return right

    left, right = binarySearchLeft(nums, target), binarySearchRight(nums, target)
    return (left, right) if left <= right else [-1, -1]

@author: zzhang
"""

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def searchRange(self, nums, target):
        left = 0
        right = len(nums)-1
        idx = -1 
        while left<=right:
            mid = (left+right)/2
            if target < nums[left]:
                return [-1,-1]
            elif target > nums[right]:
                return [-1,-1]
            elif nums[mid] == target:
                idx = mid
                break
            elif  nums[mid]  <  target <= nums[right]:
                left = mid +1 
            elif  nums[left] <= target <  nums[mid]:
                right = mid - 1 
        
        if idx == -1:
            return [-1,-1]
            
        if idx == len(nums)-1:
            i = len(nums)
        else:
            for i in range(idx,len(nums)):
                if i != len(nums)-1 and nums[i] != target:     
                    break
                elif i == len(nums)-1:
                    if nums[i] == target:
                        i = i+1
                    elif nums[i]!= target:
                        break
                        
        
        if idx == 0:
            j = -1
        else:
            for j in range(idx,-1,-1):
                if j!= 0 and nums[j] != target:
                    break
                elif j == 0:
                    if nums[j] == target:
                        j = j-1
                    elif nums[j] != target:
                        break
        return [j+1,i-1]
        
sol = Solution()
print sol.searchRange([1,1,2],1)