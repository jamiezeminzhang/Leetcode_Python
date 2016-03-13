# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 15:30:24 2016

224. Basic Calculator My Submissions Question

Total Accepted: 22889 Total Submissions: 108928 Difficulty: Medium

Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, 
non-negative integers and empty spaces .

You may assume that the given expression is always valid.

Some examples:
"1 + 1" = 2
" 2-1 + 2 " = 3
"(1+(4+5+2)-3)+(6+8)" = 23

题目中只有+ - ( )。遍历字符串，对于每个字符c：

如果是数字，则一直遍历到非数字字符，把数字找出，并与结果相加
如果是+-符号，将sign设置成对应的值
如果是(，将rt和sign压入栈中，重置rt和sign
如果是)，将sign和rt弹出栈，并计算结果


@author: Jamie
"""

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        stack = []
        num = ''
        sign = 1
        res = 0
        for i in s:
            if i.isalnum():
                num += i
            elif i == '+'or i == '-':
                res += sign*int(num) if len(num) else 0
                sign = 1 if i=='+' else -1
                num = ''
            elif i == ' ': continue
            elif i == '(':
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif i == ')':
                res += sign*int(num) if len(num) else 0
                num = ''
                res = stack.pop()*res + stack.pop()
        res += sign*int(num) if len(num) else 0
        
        return res