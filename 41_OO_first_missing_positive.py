# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 22:48:03 2016

Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.

题目给出1到N的正整数，但是不全，里面也可能混着0和负整数，找出第一个缺失的正整数。
要求时间O(N)空间固定，可使用原数组，通过交换元素使得A[i] = i + 1，
第二次遍历时不满足A[i] = i + 1的就是要找的数

@author: zeminzhang
"""

class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        length = len(A)
        for i in xrange(length):
            while A[i] != i+1:
                if A[i] <= 0 or A[i] > length or A[i] == A[A[i]-1]: break
                # swap A[i], A[A[i]-1]
                t = A[A[i]-1]; A[A[i]-1] = A[i]; A[i] = t
        for i in xrange(length):
            if A[i] != i + 1:
                return i + 1
        return length + 1

a = Solution()
print a.firstMissingPositive([3,4,-1,1])