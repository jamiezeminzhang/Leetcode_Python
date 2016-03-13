# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 08:56:18 2016

205. Isomorphic Strings My Submissions Question

Total Accepted: 46244 Total Submissions: 162014 Difficulty: Easy
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving 
the order of characters. No two characters may map to the same character but a character may map to itself.

For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.

@author: Jamie
"""

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        def strtonum(s):
            dic = {}
            num = 1
            res = ''
            for i in s:
                if i not in dic:
                    dic[i] = str(num)
                    res += str(num)
                    num += 1
                else:
                    res += dic[i]
            return res
        
        s1 = strtonum(s)
        t1 = strtonum(t)
        return True if s1==t1 else False