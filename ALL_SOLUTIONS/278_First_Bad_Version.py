# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 16:10:50 2016

278. First Bad Version

Total Accepted: 32781 Total Submissions: 149797 Difficulty: Easy

You are a product manager and currently leading a team to develop a new product. Unfortunately, 
the latest version of your product fails the quality check. Since each version is developed based 
on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes 
all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. Implement 
a function to find the first bad version. You should minimize the number of calls to the API.

@author: Jamie
"""

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=1: return 1
        
        left, right = 1, n
        while left<=right:
            mid = (left+right)/2
            if isBadVersion(mid): right = mid-1
            else: left = mid + 1
        return left