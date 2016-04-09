# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 02:18:28 2016

122. Best Time to Buy and Sell Stock II My Submissions Question

Total Accepted: 75829 Total Submissions: 184238 Difficulty: Medium
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many 
transactions as you like (ie, buy one and sell one share of the stock multiple 
times). However, you may not engage in multiple transactions at the same time 
(ie, you must sell the stock before you buy again).


@author: zeminzhang
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        length = len(prices)
        if length <=1 : return 0
        i = 0; profit = 0
        while i< length-1: 
            while i<length-1 and prices[i] >= prices[i+1]:
                i += 1
            if i < length-1:
                profit += (prices[i+1] - prices[i])
            else:
                return profit
            i += 1
        return profit
        