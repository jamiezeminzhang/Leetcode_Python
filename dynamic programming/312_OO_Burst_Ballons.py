# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 13:56:11 2016

312. Burst Balloons

Total Accepted: 5531 Total Submissions: 16074 Difficulty: Hard

Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. 
You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins.
Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note: 
(1) You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
(2) 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100

Example:

Given [3, 1, 5, 8]

Return 167

    nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
   coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167

dp[l][r]表示扎破(l, r)范围内所有气球获得的最大硬币数，不含边界；

l与r的跨度k从2开始逐渐增大；

三重循环依次枚举范围跨度k，左边界i，中点m；右边界r = i + k；


!!!!!!!!!!!!!!!!! 分段DP !!!!!!!!!!!!!!!!!

@author: zzhang04
"""

class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n==1: return nums[0]
        nums = [1] + nums + [1]
        dp = [[0 for x in range(n+2)] for y in range(n+2)]
        
        for k in range(2,n+2):
            for i in range(n+2-k):
                j = i+k
                for m in range(i+1,j):
                    dp[i][j] = max(dp[i][j], nums[i]*nums[m]*nums[j]+dp[i][m]+dp[m][j])
        
        return dp[0][n+1]