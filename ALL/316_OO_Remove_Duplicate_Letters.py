# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 17:58:13 2016

316. Remove Duplicate Letters My Submissions Question

Total Accepted: 8941 Total Submissions: 37504 Difficulty: Medium
Given a string which contains only lowercase letters, remove duplicate letters so that every 
letter appear once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

Example:
Given "bcabc"
Return "abc"

Given "cbacdcbc"
Return "acdb"

*** Another Solution  1 ***
*** DFS

def removeDuplicateLetters(self, s):
    # The order comes from here ! sorted !!!!
    for c in sorted(set(s)):
        suffix = s[s.index(c):]
        if set(suffix) == set(s):
            return c + self.removeDuplicateLetters(suffix.replace(c, ''))
    return ''

*** Another Solution 2 ***
def removeDuplicateLetters(self, s):
    result = ''
    while s:
        i = min(map(s.rindex, set(s)))
        c = min(s[:i+1])
        result += c
        s = s[s.index(c):].replace(c, '')
    return result


@author: Jamie
"""

class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        # record the last position of each letter
        rindex = {c:i for i, c in enumerate(s)}
        result = ''
        
        for i,c in enumerate(s):
            if c not in result:
                # if c < last letter in the result 
                # and there is still at least one  this letter after c
                # we can currently remove this letter and add c
                while c < result[-1:] and i < rindex[result[-1]]:
                    result = result[:-1]
                result += c
        return result