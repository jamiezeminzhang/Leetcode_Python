# -*- coding: utf-8 -*-
"""
2016/08/08 17:37 PST

340. Longest Substring with At Most K Distinct Characters 

Total Accepted: 4716
Total Submissions: 12156
Difficulty: Hard

Given a string, find the length of the longest substring T that contains at most k distinct characters.

For example, Given s = “eceba” and k = 2,

T is "ece" which its length is 3.

@author: zzhang
"""

class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        res, j, ctr = min(k, len(s)), -1, collections.defaultdict(int)
        for i, c in enumerate(list(s)):
            ctr[c] += 1
            while len(ctr)>k:
                j+=1
                ctr[s[j]]-=1
                if ctr[s[j]]==0:
                    del ctr[s[j]]
            res = max(res, i-j)
        return res