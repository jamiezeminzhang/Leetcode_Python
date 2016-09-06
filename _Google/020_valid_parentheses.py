# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 15:02:30 2015

LeetCode # 20 : Valid Parentheses

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" 
are all valid but "(]" and "([)]" are not.

@author: zzhang
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for i in s:
            if i in '([{': stack.append(i)
            elif i == ')':
                if stack and stack[-1]=='(': stack.pop()
                else: return False
            elif i == ']':
                if stack and stack[-1]=='[': stack.pop()
                else: return False
            elif i == '}':
                if stack and stack[-1]=='{': stack.pop()
                else: return False
        return True if not stack else False

sol = Solution()
print sol.isValid("[([]])")