# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 08:12:26 2016

131. Palindrome Partitioning My Submissions Question

Total Accepted: 58009 Total Submissions: 211642 Difficulty: Medium
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

  [
    ["aa","b"],
    ["a","a","b"]
  ]

@author: zeminzhang
"""

class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        def ispalindrome(s):
            length = len(s)
            for i in range(length/2):
                if s[i] != s[length-1-i]: return False
            return True
        
        def dfs(s, reslist):
            length = len(s)
            if length == 0: res.append(reslist)
            else:
                for i in range(1,length+1):
                    if ispalindrome(s[:i]):
                        dfs(s[i:], reslist+[s[:i]] )
        res = []
        dfs(s,[])
        return res