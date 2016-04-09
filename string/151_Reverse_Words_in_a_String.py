# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 09:37:14 2016

151. Reverse Words in a String

Total Accepted: 90312 Total Submissions: 580145 Difficulty: Medium

Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".

@author: zeminzhang
"""

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == len(s)*' ': return ''
        tmp = s.split(' ')
        i = 0
        while i < len(tmp):
            if tmp[i] == len(tmp[i])*' ':  # remove all the spaces in tmp
                del tmp[i]
            else:
                i+=1
        tmp.reverse()
        return ' '.join(tmp)