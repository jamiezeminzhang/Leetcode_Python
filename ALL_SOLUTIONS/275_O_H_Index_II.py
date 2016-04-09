# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 16:03:29 2016

275. H-Index II My Submissions Question

Total Accepted: 18322 Total Submissions: 56764 Difficulty: Medium
Follow up for H-Index: What if the citations array is sorted in ascending order? Could you optimize your algorithm?

Hint:

Expected runtime complexity is in O(log n) and the input is sorted.

@author: Jamie
"""

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations: return 0
        length = len(citations)
        if length == 1: return 0 if citations[0]==0 else 1
        left, right = 0, length-1
        
        while left<=right:
            mid = (left+right)/2
            print (left, mid, right)
            if length-mid == citations[mid]:
                return length-mid
            elif length-mid > citations[mid]:
                left = mid+1
            else:
                right = mid-1
            print (left, right)
        return length-left
            