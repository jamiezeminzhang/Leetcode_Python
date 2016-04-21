# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 22:59:20 2016

121. Best Time to Buy and Sell Stock

Total Accepted: 84382 Total Submissions: 240817 Difficulty: Medium

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one 
and sell one share of the stock), design an algorithm to find the maximum profit.

# The given solution is O(n)
My initial thought was O(n^2)

@author: zeminzhang
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices == []: return 0
        length, profit, low = len(prices), 0 , 2**31-1
        for i in range(length):
            if prices[i] < low: low = prices[i]
            profit = max( prices[i] - low, profit)
        return profit
        