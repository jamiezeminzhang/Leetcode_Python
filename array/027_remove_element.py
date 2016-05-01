# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 15:22:17 2015

LeetCode # 27 Remove Element

Given an array and a value, remove all instances of that value in place and return the new length.

The order of elements can be changed. It doesn't matter what you leave beyond the new length. 

之所以不用remove or delete 之类的是因为他们的复杂度都是O(n).所以整体复杂度是O(n^2).

只用交换的话，整体复杂度是O(n).

@author: zzhang
"""

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i, j = 0, len(nums)-1
        while i<=j:
            if nums[i] == val:
                nums[i], nums[j] = nums[j], nums[i]
                j-=1
            else: i+=1
        return i

sol = Solution()
print sol.removeElement([3,3,3,3],4)