# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 10:20:10 2016

301. Remove Invalid Parentheses

Total Accepted: 8733 Total Submissions: 28115 Difficulty: Hard

Remove the minimum number of invalid parentheses in order to make the input string valid. 
Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Examples:
"()())()" -> ["()()()", "(())()"]
"(a)())()" -> ["(a)()()", "(a())()"]
")(" -> [""]

@author: Jamie
"""

class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        q, ans, visited = {s}, [], set()
        min_num_reached = False
        while q:
            ans = filter(self.isValidParentheses, q)
            if ans: return ans
            q = {cur[:i]+cur[i+1:] for cur in q for i in xrange(len(cur))}
        return ans
        
    def isValidParentheses(self, s):
        count = 0
        for i in s:
            if i == '(': count += 1
            if i == ')':
                if count == 0: return False
                count -= 1
        return count == 0
    