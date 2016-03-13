# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 03:31:05 2016

123. Best Time to Buy and Sell Stock III My Submissions Question
Total Accepted: 50754 Total Submissions: 198691 Difficulty: Hard
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell 
the stock before you buy again).

# My first solution is O(n^2) which simply separates the prices into two list
# Surely, TLE

# Correct solution:
解题思路：只允许做两次交易，这道题就比前两道要难多了。解法很巧妙，有点动态规划的意思：
开辟两个数组f1和f2，f1[i]表示在price[i]之前进行一次交易所获得的最大利润，
f2[i]表示在price[i]之后进行一次交易所获得的最大利润。则f1[i]+f2[i]的最大值就是所要求的最大值，
而f1[i]和f2[i]的计算就需要动态规划了，看代码不难理解。

# 注意f2的算法。。。好巧妙

@author: zeminzhang
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        length = len(prices)
        if length <= 1: return 0
        f1 = [0 for x in range(length)]
        f2 = [0 for x in range(length)]
        
        res, profit1, profit2 = 0,0,0
        low, high = prices[0], prices[-1]
        for i in range(1,length):
            low = min(low, prices[i])
            f1[i] = max(f1[i-1], prices[i]-low)
        for i in range(length-2,-1,-1):
            high = max(high, prices[i])
            f2[i] = max(f2[i+1], high-prices[i])
            
        for i in range(length):
            if f1[i]+f2[i] > res: res = f1[i]+f2[i]
        return res