# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 09:46:37 2016

@author: zeminzhang
"""

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        if length == 0: return 0
        
        t = s.split()
        if len(t) == 0: return 0
        return len(t[-1])
        
        
        
sol = Solution()
print sol.lengthOfLastWord('I love you')
print sol.lengthOfLastWord(' ')