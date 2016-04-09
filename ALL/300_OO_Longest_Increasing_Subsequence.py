# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 22:19:30 2016

300. Longest Increasing Subsequence My Submissions Question

Total Accepted: 18184 Total Submissions: 54341 Difficulty: Medium
Given an unsorted array of integers, find the length of longest increasing subsequence.

For example,
Given [10, 9, 2, 5, 3, 7, 101, 18],
The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4. Note that there may be more than one LIS combination, it is only necessary for you to return the length.

Your algorithm should run in O(n2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?

Solution 1: DP as given

class Solution(object):
    def lengthOfLIS(self, nums):
        length = len(nums)
        
        dp = [1]*length
        for i in xrange(1,length):
            for j in xrange(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp) if dp else 0
        
Solution 2: O(n * log n)解法（运行时间44ms）：
维护一个单调序列
遍历nums数组，二分查找每一个数在单调序列中的位置，然后替换之。

class Solution(object):
    def lengthOfLIS(self, nums):
        size = len(nums)
        dp = []
        for x in range(size):
            low, high = 0, len(dp) - 1
            while low <= high:
                mid = (low + high) / 2
                if dp[mid] >= nums[x]:
                    high = mid - 1
                else:
                    low = mid + 1
            if low >= len(dp):
                dp.append(nums[x])
            else:
                dp[low] = nums[x]
        return len(dp)

@author: Jamie
"""

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = []
        for num in nums:
            left, right = 0, len(dp)-1
            while left<=right:
                mid = (left+right)/2
                if num <= dp[mid]:
                    right = mid-1
                else:
                    left = mid+1
            if left>=len(dp):
                dp.append(num)
            else:
                dp[left] = num
        return len(dp)

sol = Solution()
print sol.lengthOfLIS([10,9,2,5,3,7,101,18,20])