# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 06:37:48 2016

209. Minimum Size Subarray Sum My Submissions Question

Total Accepted: 31399 Total Submissions: 120310 Difficulty: Medium
Given an array of n positive integers and a positive integer s, find the minimal length of a 
subarray of which the sum ≥ s. If there isn't one, return 0 instead.

For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint.

click to show more practice.

More practice:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).

*** Even for the O(n) solution, I need to think about it more carefully.
*** Conditions & pointers
*** Here is the O(n) solution of myself
class Solution(object):
    def minSubArrayLen(self, s, nums):
        max_sum = sum(nums)
        if max_sum < s: return 0
        max_num = max(nums)
        if max_num >= s: return 1
        
        length = len(nums)
        lis = [nums[-1] for x in range(length)]
        for i in range(length-2,-1,-1):
            lis[i] = lis[i+1]+nums[i]
        
        p1=0; p2 = 1
        res = length
        while p1<length:
            if p2 < length and lis[p1] - lis[p2]<s:
                p2+=1
            else:
                if p2!= length:
                    res = min(res, p2-p1) if lis[p1] - lis[p2]>=s else res
                else:
                    res = min(res, length-p1) if lis[p1] >=s else res
                p1+=1
        return res

For the O(nlogn) algorithm, given below. Using the idea of binary search.

@author: Jamie
"""

class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        max_sum = sum(nums)
        if max_sum < s: return 0
        max_num = max(nums)
        if max_num >= s: return 1
        
        length = len(nums)
        lis = [nums[-1] for x in range(length)]
        for i in range(length-2,-1,-1):
            lis[i] = lis[i+1]+nums[i]
        lis += [0]
        
        res = length
        for i in range(length):
            left = i+1; right = length
            while left <= right:
                mid = (left+right)/2
                if lis[i] - lis[mid] >= s:
                    res = min(res, mid-i)
                    right = mid-1
                else:
                    left = mid+1
        return res

sol = Solution()
print sol.minSubArrayLen(11,[1,2,3,4,5])
#print sol.minSubArrayLen(4,[1,4,4])
#print sol.minSubArrayLen(15,[5,1,3 ,5,10,7,4,9,2,8])

