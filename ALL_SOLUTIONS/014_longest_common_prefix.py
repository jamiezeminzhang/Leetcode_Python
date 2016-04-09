# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 15:29:19 2015

LeetCode #14 Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings. 

class Solution:
    # @param {string[]} strs
    # @return {string}
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""
            
        common = ""
        for i in range(len(strs[0])):
            cha = strs[0][i]
            for j in range(len(strs)):
                temp = strs[j]
                if i>=len(temp) or temp[i]!=cha:
                    return common
            common += cha
        return common
@author: zzhang
"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]; rtype: str
        """
        sz, ret = zip(*strs), ""
        # looping corrected based on @StefanPochmann's comment below
        print sz
        for c in sz:
            if len(set(c)) > 1: break
            ret += c[0]
        return ret
        
def foo(*args):
     for a in args:
         print a
sol = Solution()
print sol.longestCommonPrefix(['abc','abcde','abcsx'])