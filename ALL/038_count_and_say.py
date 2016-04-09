# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 20:43:27 2016

38. Count and Say My Submissions Question
Total Accepted: 67004 Total Submissions: 245260 Difficulty: Easy
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
        if n==1:
            return '1'
        if n==2:
            return '11'
        if n==3:
            return '21'
        
        if n>=4:
            res = self.countAndSay(n-1)
            i=0
            count = 1
            r = ''
            while i<len(res):
                if i>=1 and res[i] == res[i-1]:
                    count += 1
                    i += 1
                if i>=1 and res[i] != res[i-1]:
                    r = r+str(count)+res[i-1]
                    i += 1
                    count = 0
        return r

sol = Solution()