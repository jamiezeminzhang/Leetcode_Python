# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 11:19:35 2016

345. Reverse Vowels of a String

Total Accepted: 2206 Total Submissions: 5991 Difficulty: Easy

Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".


*** StefanPochman's answer ***

def reverseVowels(self, s):
    vowels = re.findall('(?i)[aeiou]', s)
    return re.sub('(?i)[aeiou]', lambda m: vowels.pop(), s)
    
It's possible in one line, but I don't really like it:

def reverseVowels(self, s):
    return re.sub('(?i)[aeiou]', lambda m, v=re.findall('(?i)[aeiou]', s): v.pop(), s)
    



@author: Jamie
"""

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        v, s_list = '', list(s)
        for i in s: 
            if i in 'aeiouAEIOU': v += i
        for idx in range(len(s_list)):
            if s_list[idx] in 'aeiouAEIOU':
                s_list[idx] = v[-1]
                v = v[:-1]
        return ''.join(s_list)