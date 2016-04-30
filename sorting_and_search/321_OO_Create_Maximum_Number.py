# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 10:22:09 2016

321. Create Maximum Number

Total Accepted: 3549 Total Submissions: 18030 Difficulty: Hard

Given two arrays of length m and n with digits 0-9 representing two numbers. 
Create the maximum number of length k <= m + n from digits of the two. 
The relative order of the digits from the same array must be preserved. 
Return an array of the k digits. You should try to optimize your time and space complexity.

Example 1:
nums1 = [3, 4, 6, 5]
nums2 = [9, 1, 2, 5, 8, 3]
k = 5
return [9, 8, 6, 5, 3]

Example 2:
nums1 = [6, 7]
nums2 = [6, 0, 4]
k = 5
return [6, 7, 6, 0, 4]

Example 3:
nums1 = [3, 9]
nums2 = [8, 9]
k = 3
return [9, 8, 9]


解题思路：
问题可以转化为这样的两个子问题：

1. 从数组nums中挑选出t个数，在保持元素相对顺序不变的情况下，使得选出的子数组最大化。

2. 在保持元素相对顺序不变的前提下，将数组nums1与数组nums2合并，使合并后的数组最大化。

merge函数可以简化成一行：

参考：https://leetcode.com/discuss/75804/short-python

def merge(nums1, nums2):
    return [max(nums1, nums2).pop(0) for _ in nums1 + nums2]
    
@author: Jamie
"""

class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        def getMax(nums, t):
            ans = []
            length = len(nums)
            for i in xrange(length):
                while ans and ans[-1]<nums[i] and len(ans) + length - i > t:
                    ans.pop()
                if len(ans)<t:
                    ans += nums[i],
            return ans
        
        def merge(nums1,nums2):
            ans = []
            while nums1 or nums2:
                if nums1 > nums2:
                    ans += nums1[0],
                    nums1 = nums1[1:]
                else:
                    ans += nums2[0],
                    nums2 = nums2[1:]
            return ans
        
        l1, l2 = len(nums1), len(nums2)
        res = []
        for i in xrange( max(0, k-l2), min(k,l1)+1 ):
            r1 = getMax(nums1, i)
            r2 = getMax(nums2, k-i)
            r = merge(r1,r2)
            res = max(res, r)
        return res
        