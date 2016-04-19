# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 16:56:51 2016

343. Integer Break 

Total Accepted: 1005 Total Submissions: 2325 Difficulty: Medium

Given a positive integer n, break it into the sum of at least two positive integers and maximize the 
product of those integers. Return the maximum product you can get.

For example, given n = 2, return 1 (2 = 1 + 1); given n = 10, return 36 (10 = 3 + 3 + 4).

Note: you may assume that n is not less than 2.

Hint:

There is a simple O(n) solution to this problem.
You may check the breaking results of n ranging from 7 to 10 to discover the regularities.

**** A O(1) solution ***

def integerBreak(self, n):
    return n - 1 if n < 4 else 3**((n-2)/3) * ((n-2)%3+2)

@author: Jamie
"""

class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0,0,1,2,4,6,9]
        for i in range(7,n+1): dp += max(3*dp[i-3], 2*dp[i-2]),
        return dp[n]