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
        vowels, slist = [], list(s)
        for letter in s:
            if letter in 'aeiouAEIOU':
                vowels.append(letter)
        for idx, letter in enumerate(slist):
            if letter in 'aeiouAEIOU':
                slist[idx] = vowels.pop()
        return ''.join(slist)