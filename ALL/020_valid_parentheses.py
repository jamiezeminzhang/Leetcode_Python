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

class Solution:
    # @param {string} s
    # @return {boolean}
    def isValid(self, s):
        if len(s) == 0:
            return True
        if len(s) == 1:
            return False
        
        stack = [];
        
        for i in s:
            if i =='(' or i=='{' or i =='[':
                stack.append(i)
                print stack
            else:
                numLen = len(stack)
                if numLen == 0 :
                    return False
                if i == ')':
                    if stack[numLen-1] == '(':
                        stack.pop()
                    else:
                        return False
                if i == ']':
                    if stack[numLen-1] == '[':
                        stack.pop()
                    else:
                        return False
                if i == '}':
                    if stack[numLen-1] == '{':
                        stack.pop()
                    else:
                        return False
                print stack
        
        if len(stack)!=0:
            return False
        else:
            return True

sol = Solution()
print sol.isValid("[([]])")