# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 14:52:25 2015

LeetCode #5: Longest Palindromic Substring 

Given a string S, find the longest palindromic substring in S. 
You may assume that the maximum length of S is 1000, 
and there exists one unique longest palindromic substring.

@author: zzhang
"""

"""

Following is done in O(n^2) time and O(n^2) space 
DP

class Solution:
    # @param {string} s
    # @return {string}
    def longestPalindrome(self, s):
        n = len(s)
        t = [[False for i in range(n)] for j in range(n)]
        start = 0
        max_len = 1
        for i in range(n):
            t[i][i] = True
        
        for i in range(n-1):
            j = i+1
            if s[i]==s[j]:
                t[i][j] = True
                start = i
                max_len = 1
        
        for l in range(3,n+1):
            for i in range(n-l+1):
                j = i+l-1
                if (s[i]==s[j]) and t[i+1][j-1]:
                    t[i][j] = True
                    start = i
                    max_len = l
        
        return s[start:start+max_len]
===============================================================================
O(n) Solution: Manacher's algorithm

http://articles.leetcode.com/2011/11/longest-palindromic-substring-part-ii.html

===============================================================================
"""

class Solution:
    # @param {string} s
    # @return {string}
    def longestPalindrome(self, s):
        T = self.preProcess(s)
        n = len(T)
        P = [0 for x in range(n)]
        
        # center and right edge
        C = 0
        R = 0
        
        for i in range(1,n-1):
            i_mirror = 2*C-i
            
            P[i] = P[i_mirror] if P[i_mirror] < (R-i) else (R-i)
            
            
            while T[i+1+P[i]] == T[i-1-P[i]]:
                P[i] += 1
            
            if i+P[i]>R:
                C = i
                R = i+P[i]
            
        maxLen = max(P)
        center = [i for i,j in enumerate(P) if j == maxLen]
        center = center[0]
        
        #print maxLen
        #print center
        
        start_point = (center - 1 - maxLen)/2
        end_point   = start_point+maxLen
        
        return s[start_point:end_point]
    
    
    def preProcess(self, s):
        T = "^#"
        for i in s:
            T = T + i + "#"
        
        T = T+"$"
        return T
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        