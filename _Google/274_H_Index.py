# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 15:18:59 2016

274. H-Index

Total Accepted: 25892 Total Submissions: 90252 Difficulty: Medium

Given an array of citations (each citation is a non-negative integer) of a researcher, 
write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her 
N papers have at least h citations each, and the other N − h papers have no more than h citations each."

For example, given citations = [3, 0, 6, 1, 5], which means the researcher has 5 papers in total 
and each of them had received 3, 0, 6, 1, 5 citations respectively. Since the researcher has 3 papers 
with at least 3 citations each and the remaining two with no more than 3 citations each, his h-index is 3.

Note: If there are several possible values for h, the maximum one is taken as the h-index.

Hint:

An easy approach is to sort the array first.
What are the possible values of h-index?
A faster approach is to use extra space.

Following is the solution with extra space and no sorting involved. Idea is histogram.

class Solution(object):
    def hIndex(self, citations):
        if not citations: return 0
        length = len(citations)
        his = [0]*(length+1)
        
        for c in citations:
            if c<=length: his[c] += 1
            else: his[length] += 1
        
        total = 0
        for i in xrange(length,-1,-1):
            total += his[i]
            if total>=i: return i
        return 0
        

@author: Jamie
"""

# Following is the sort solution without extra space
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations: return 0
        citations.sort()
        length = len(citations)
        for i in xrange(length):
            if citations[i]>=length-i: return length - i
        return 0