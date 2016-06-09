# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 09:46:37 2016

58. Length of Last Word

Total Accepted: 96077 Total Submissions: 324909 Difficulty: Easy

Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

For example, 
Given s = "Hello World",
return 5.
@author: zeminzhang
"""

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        t = s.split()
        if len(t) == 0: return 0
        return len(t[-1])
        
        
        
sol = Solution()
print sol.lengthOfLastWord('I love you')
print sol.lengthOfLastWord(' ')