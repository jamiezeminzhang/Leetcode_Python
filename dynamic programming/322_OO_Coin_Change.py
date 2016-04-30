# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 12:58:24 2016

322. Coin Change

Total Accepted: 12851 Total Submissions: 52208 Difficulty: Medium

You are given coins of different denominations and a total amount of money amount. 
Write a function to compute the fewest number of coins that you need to make up that amount. 
If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:
coins = [1, 2, 5], amount = 11
return 3 (11 = 5 + 5 + 1)

Example 2:
coins = [2], amount = 3
return -1.

** 直接双重循环是 O（n^2） 的复杂度
** 下面的方法是 O(nk) 的复杂度

@author: Jamie
"""

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [0] + [-1]*amount
        for x in range(amount):
            if dp[x]== -1:
                continue
            for c in coins:
                if x+c>amount:
                    continue
                if dp[x+c]<0 or dp[x+c]>dp[x]+1:
                    dp[x+c] = dp[x]+1
        return dp[amount]
            
            
            