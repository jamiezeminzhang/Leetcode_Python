# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 17:25:56 2015

LeetCode 33 Search in Rotated Sorted Array

Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index,
 otherwise return -1.

You may assume no duplicate exists in the array.

@author: zzhang
"""

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        left = 0
        right = len(A) - 1
        while left <= right:
            mid = (left + right) / 2
            if A[mid] == target:
                return mid
            if A[mid] >= A[left]:
                # the left part is monotonically increasing 
                # A[mid] may equal to A[left], e.g. A=[3,1] target=1
                if A[left] <= target < A[mid]:
                    # A[left] may equal to target, e.g. A=[4,5,6,7,0,1,2] target=0
                    right = mid - 1
                else:
                    left = mid + 1
            else: # the right part is monotonically increasing
                if A[mid] < target <= A[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1