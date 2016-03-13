# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 10:07:19 2015

LeetCode #3 Longest Substring Without Repeating Characters

Given a string, find the length of the longest substring without repeating characters.
 For example, the longest substring without repeating letters for "abcabcbb" is "abc", 
 which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.


@author: zzhang
"""

class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstring(self, s):
        res = 0
        cur = 0
        d = {}
        for i, c in enumerate(s):
            if c not in d:
                cur += 1
            else:
                cur = min(i - d[c], cur + 1)
            d[c] = i
            res = max(res, cur)
        return res

sol = Solution()
print sol.lengthOfLongestSubstring("abcad")