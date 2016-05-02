# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 22:48:03 2016

41. First Missing Positive

Total Accepted: 63492 Total Submissions: 266615 Difficulty: Hard

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

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        for i in range(length):
            while nums[i] != i+1:
                if nums[i] <= 0 or nums[i] > length or nums[i] == nums[nums[i]-1]: break
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
        for i in range(length):
            if nums[i] != i + 1:return i + 1
        return length + 1

a = Solution()
print a.firstMissingPositive([3,4,-1,1])