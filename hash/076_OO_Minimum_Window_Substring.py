# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 02:43:32 2016

76. Minimum Window Substring

Total Accepted: 51959 Total Submissions: 254513 Difficulty: Hard

Given a string S and a string T, find the minimum window in S which will 
contain all the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the 
empty string "".

If there are multiple such windows, you are guaranteed that there will always 
be only one unique minimum window in S.

解题思路：双指针思想，尾指针不断往后扫，当扫到有一个窗口包含了所有T的字符，然后再收缩头指针，
直到不能再收缩为止。最后记录所有可能的情况中窗口最小的。

@author: zeminzhang
"""
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        counter_dict = collections.Counter(t)
        count = len(t)
        start, min_start, min_size = 0, 0, 1000000
        for end, c in enumerate(s):
            if c in counter_dict:
                counter_dict[c] -= 1
                if counter_dict[c] >= 0:
                    count -= 1
            if count == 0:
                while True:
                    if s[start] in counter_dict:
                        if counter_dict[s[start]]<0:
                            counter_dict[s[start]]+=1
                        else:
                            break
                    start += 1
                if min_size > end-start+1:
                    min_size = end-start+1
                    min_start = start
        if min_size == 1000000: return ''
        else: return s[min_start:min_start+min_size]