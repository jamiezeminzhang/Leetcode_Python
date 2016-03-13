# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 02:43:32 2016

76. Minimum Window Substring My Submissions Question
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

class Solution:
    # @return a string
    def minWindow(self, S, T):
        count1={}; count2={}
        for char in T:
            if char not in count1: count1[char]=1
            else: count1[char]+=1
        for char in T: # count2 just for counting, never changed
            if char not in count2: count2[char]=1
            else: count2[char]+=1
        count=len(T)
        start=0; minSize=100000; minStart=0
        for end in range(len(S)):
            if S[end] in count2 and count2[S[end]]>0:
                count1[S[end]]-=1
                if count1[S[end]]>=0:
                    count-=1
            if count==0:
                while True:
                    if S[start] in count2 and count2[S[start]]>0:
                        if count1[S[start]]<0: # over deleted. we could move the start ahead
                            count1[S[start]]+=1
                        else:
                            break
                    start+=1
                if minSize>end-start+1:
                    minSize=end-start+1; minStart=start
        if minSize==100000: return ''
        else:
            return S[minStart:minStart+minSize]