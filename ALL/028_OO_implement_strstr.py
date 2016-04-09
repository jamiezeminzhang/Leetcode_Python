# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 13:27:26 2015

LeetCode # 28: Implement strStr()

 Implement strStr().

Returns the index of the first occurrence of needle in haystack, or -1 if 
needle is not part of haystack.

Update (2014-11-02):
The signature of the function had been updated to return the index instead of 
the pointer. If you still see your function signature returns a char * or 
String, please click the reload button to reset your code definition. 

@author: zzhang
"""

class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return a string or None
    def strStr(self, haystack, needle):
        if len(haystack) < len(needle): return -1
        i = 0
        while i < len(haystack)-len(needle)+1:
            j = 0; k = i
            while j < len(needle):
                if haystack[k] == needle[j]:
                    j+=1; k+=1
                else:
                    break
            if j == len(needle):
                break
            else:
                i+=1
        if i == len(haystack)-len(needle)+1:
            return -1
        else:
            return i