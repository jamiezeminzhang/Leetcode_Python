# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 16:20:48 2015

LeetCode # 32: Longest Valid Parentheses

Given a string containing just the characters '(' and ')', find the length 
of the longest valid (well-formed) parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has length = 2.

Another example is ")()())", where the longest valid parentheses substring 
is "()()", which has length = 4. 

@author: zzhang
"""

class Solution:
    # @param {string} s
    # @return {integer}
    def longestValidParentheses(self, s):
        # 记录左括号的index，每次出现右括号且可以跟栈顶左括号匹配时，更新一下maxLen
        # stack[-1] is the top entry of the stack
        stack, maxLen = [-1], 0
        for i in xrange(len(s)):
            if s[i] == ')' and stack[-1] != -1 and s[stack[-1]] == '(':
                stack.pop()
                maxLen = max(maxLen, i - stack[-1]) # 一共连续弹出去多少个括hao
            else:
                stack.append(i)
        return maxLen

test = ['(',')']
sol  = Solution();
print sol.longestValidParentheses(test)
