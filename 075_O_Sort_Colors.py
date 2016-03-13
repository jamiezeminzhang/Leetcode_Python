# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 02:14:43 2016

75. Sort Colors My Submissions Question
Total Accepted: 84798 Total Submissions: 249912 Difficulty: Medium
Given an array with n objects colored red, white or blue, sort them so that 
objects of the same color are adjacent, with the colors in the order red, 
white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, 
and blue respectively.

Note:
You are not suppose to use the library's sort function for this problem.

click to show follow up.

Follow up:
A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite 
array with total number of 0's, then 1's and followed by 2's.

Could you come up with an one-pass algorithm using only constant space?


@author: zeminzhang
"""

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        left, right = 0, len(nums)-1
        i = 0
        while i<right+1:
            if nums[i] == 0:
                tmp = nums[left]
                nums[left] = nums[i]
                nums[i] = tmp
                left += 1
                i += 1
                continue
            if nums[i] == 2:
                tmp = nums[right]
                nums[right] = nums[i]
                nums[i] = tmp
                right -= 1
                continue
            i +=1
        
#        return nums

#sol = Solution()
#print sol.sortColors([0,1,0,2,1,1,0,2,2])