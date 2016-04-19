# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 16:48:52 2016

227. Basic Calculator II

Total Accepted: 17726 Total Submissions: 74704 Difficulty: Medium

Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . 
The integer division should truncate toward zero.

You may assume that the given expression is always valid.

Some examples:
"3+2*2" = 7
" 3/2 " = 1
" 3+5 / 2 " = 5
Note: Do not use the eval built-in library function.

分两次遍历，第一次遍历时，遇到乘除符号就计算；第二次遍历，计算加减符号。

@author: Jamie
"""

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        num = ''
        for i in s:
            if i == ' ': continue
            elif i.isalnum():
                num += i
            else:
                stack.append(int(num))
                stack.append(i)
                num = ''
        stack.append(int(num))
        
        length = len(stack)
        i = 1
        k = 0
        while i<length-1-k:
            if stack[i] == '*' or stack[i] =='/':
                if stack[i] == '*':
                    stack[i-1] = stack[i-1]*stack[i+1]
                if stack[i] == '/':
                    stack[i-1] = stack[i-1]/stack[i+1]
                del stack[i]
                del stack[i]  # not i+1
                k+=2
            else:
                i += 1
        res = 0
        sign = 1
        for j in stack:
            if j == '+':
                sign = 1
            elif j == '-':
                sign = -1
            else:
                res += sign*int(j)
        return res
                    
        