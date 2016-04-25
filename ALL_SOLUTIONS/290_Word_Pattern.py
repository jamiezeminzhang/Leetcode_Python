# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 17:21:47 2016

290. Word Pattern

Total Accepted: 26375 Total Submissions: 93875 Difficulty: Easy

Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Examples:
pattern = "abba", str = "dog cat cat dog" should return true.
pattern = "abba", str = "dog cat cat fish" should return false.
pattern = "aaaa", str = "dog cat cat dog" should return false.
pattern = "abba", str = "dog dog dog dog" should return false.
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.

A much shorter solution which uses exactly the same idea:

def wordPattern(self, pattern, str):
    s = pattern
    t = str.split()
    return map(s.find, s) == map(t.index, t)

@author: Jamie
"""

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str = str.split(' ')
        dic1, dic2 = {}, {}
        count1, count2 = 0, 0
        res1, res2 = [], []
        
        for i in pattern:
            if i not in dic1:
                res1.append(count1)
                dic1[i] = count1
                count1 += 1
            else:
                res1.append(dic1[i])
            
        for i in str:
            if i not in dic2:
                res2.append(count2)
                dic2[i] = count2
                count2 += 1
            else:
                res2.append(dic2[i])
        return res1==res2