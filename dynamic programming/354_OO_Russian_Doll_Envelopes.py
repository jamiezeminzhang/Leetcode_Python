# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 09:14:59 2016

354. Russian Doll Envelopes

Total Accepted: 1060 Total Submissions: 3840 Difficulty: Hard

You have a number of envelopes with widths and heights given as a pair of integers (w, h). One envelope can fit into another if and only if both the width and height of one envelope is greater than the width and height of the other envelope.

What is the maximum number of envelopes can you Russian doll? (put one inside other)

Example:
Given envelopes = [[5,4],[6,4],[6,7],[2,3]], the maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).

# Given is O(nlonn) solution
# Following is TLE DP O(n^2) solution. Could pass in C++ but not in Python.
In the middle of an interview DP solution may be better.

class Solution(object):
    def maxEnvelopes(self, envelopes):
        n = len(envelopes)
        if n==0 or n == 1: return n
        
        dp = [1 for i in range(n)]
        envelopes.sort()
        for i in range(n):
            for j in range(i):
                if envelopes[i][0]>envelopes[j][0] and \
                envelopes[i][1]>envelopes[j][1]:
                    dp[i] == max(dp[i], dp[j]+1)
        return dp[-1]

@author: zeminzhang
"""

class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        def bin_search(v, a):
            left, right = 0, len(v)
            while left<right:
                mid = (left + right)/2
                if v[mid][1]<a[1]: left = mid+1
                else: right = mid
            return left
        envelopes.sort(cmp = lambda x,y: x[0]-y[0] if x[0] != y[0] else y[1]-x[1])
        res = []
        for i in envelopes:
            p = bin_search(res, i)
            if p == len(res): res.append(i)
            else: res[p] = i
        return len(res)