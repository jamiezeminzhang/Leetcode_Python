# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 22:13:07 2016

119. Pascal's Triangle II My Submissions Question
Total Accepted: 65337 Total Submissions: 208879 Difficulty: Easy
Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?
Yes of course I can:)

@author: zeminzhang
"""

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0: return [1]
        if rowIndex == 1: return [1,1]
        tmp = [0]+self.getRow(rowIndex-1)+[0]
        for i in range(rowIndex+1):
            tmp[i] = tmp[i]+tmp[i+1]
        return tmp[:-1]
        