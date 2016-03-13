# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 23:13:37 2016

309. Best Time to Buy and Sell Stock with Cooldown My Submissions Question
Total Accepted: 9203 Total Submissions: 25713 Difficulty: Medium
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:

prices = [1, 2, 3, 0, 2]
maxProfit = 3
transactions = [buy, sell, cooldown, buy, sell]

解法II：

引入辅助数组sells和buys

sells[i]表示在第i天不持有股票所能获得的最大累计收益
buys[i]表示在第i天持有股票所能获得的最大累计收益

初始化数组：
sells[0] = 0
sells[1] = max(0, prices[1] - prices[0])
buys[0] = -prices[0]
buys[1] = max(-prices[0], -prices[1])
状态转移方程：

sells[i] = max(sells[i - 1], buys[i - 1] + prices[i])
buys[i] = max(buys[i - 1], sells[i - 2] - prices[i])

@author: Jamie
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        length = len(prices)
        if length <=1: return 0
        if length ==2: return max(0,prices[1]-prices[0])
        buys  = [None]*length
        sells = [None]*length
        buys[0] = -prices[0]; buys[1] = max(-prices[0],-prices[1])
        sells[0]= 0; sells[1] = max(prices[1]-prices[0],0)
        
        for i in range(2,length):
            sells[i] = max(buys[i-1]+prices[i], sells[i-1])
            buys[i] = max(sells[i-2]-prices[i],buys[i-1] )
        return sells[-1]