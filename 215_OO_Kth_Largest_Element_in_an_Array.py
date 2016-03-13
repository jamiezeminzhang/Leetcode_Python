# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 17:20:03 2016

215. Kth Largest Element in an Array My Submissions Question
Total Accepted: 41976 Total Submissions: 132522 Difficulty: Medium
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the 
sorted order, not the kth distinct element.

For example,
Given [3,2,1,5,6,4] and k = 2, return 5.

Note: 
You may assume k is always valid, 1 ≤ k ≤ array's length.

*** 用random比我不用random直接用nums[0]快好多啊。。。
import random
class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer}
    def findKthLargest(self, nums, k):
        pivot = random.choice(nums)
        nums1, nums2 = [], []
        for num in nums:
            if num > pivot:
                nums1.append(num)
            elif num < pivot:
                nums2.append(num)
        if k <= len(nums1):
            return self.findKthLargest(nums1, k)
        if k > len(nums) - len(nums2):
            return self.findKthLargest(nums2, k - (len(nums) - len(nums2)))
        return pivot
        
@author: Jamie
"""

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        length = len(nums)
        if length == 1 and k == 1: return nums[0]
        
        nums1,nums2 = [],[]
        pivot = nums[0]
        for num in nums[1:]:
            if num<pivot: nums2.append(num)
            if num>pivot: nums1.append(num)
        
        if k<= len(nums1)  : return self.findKthLargest(nums1,k)
#        if k > len(nums1)+1: return self.findKthLargest(nums2, k - ( len(nums)+1 ))  # 可能有和pivot相等的情况所以不能用这个
        if k>length-len(nums2): return self.findKthLargest(nums2, k-(len(nums) - len(nums2)))
        return pivot
        
sol = Solution()
print sol.findKthLargest([2,1],1)