# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 20:43:27 2016

38. Count and Say

Total Accepted: 67004 Total Submissions: 245260 Difficulty: Easy
0
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.

@author: zeminzhang
"""

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n==1:return '1'
        if n>=2:
            res = self.countAndSay(n-1)
            i,  r = 0, ''
            while i<len(res):
                count = 1
                while i<len(res)-1 and res[i] == res[i+1]:
                    count+=1; i+=1
                r += str(count)+res[i]
                i += 1
        return r