# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 16:11:53 2016

279. Perfect Squares

Total Accepted: 25738 Total Submissions: 82018 Difficulty: Medium

Given a positive integer n, find the least number of perfect square numbers 
(for example, 1, 4, 9, 16, ...) which sum to n.

For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.

Idea is here, AC in C++ but TLE in python

class Solution(object):
    def numSquares(self, n):
        dp = collections.defaultdict(int)
        y = 1
        while y * y <= n:
            dp[y * y] = 1
            y += 1
        for x in range(1, n + 1):
            y = 1
            while x + y * y <= n:
                if x + y * y not in dp or dp[x] + 1 < dp[x + y * y]:
                    dp[x + y * y] = dp[x] + 1
                y += 1
        return dp[n]
        

**** The reason that the following codes work is *****
by StefanPochman
There are so many "large" test cases that it's worthwhile to keep data between test cases rather than recomputing 
from scratch all the time.

其实就是把之前test的时候得到的dp的结果存到Solution这个class里。下次test更大的数的时候不需要从头算，直接从self._dp里取出来就好。

@author: Jamie
"""
class Solution(object):
    _dp = [0]
    def numSquares(self, n):
        dp = self._dp
        while len(dp) <= n:
            # dp += min( dp[-1], dp[-4], dp[-9],...) + 1
            dp += min(dp[-i*i] for i in range(1, int(len(dp)**0.5+1))) + 1,
        return dp[n]
        
sol = Solution()
print sol.numSquares(1423128)