# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 09:02:55 2016

150. Evaluate Reverse Polish Notation My Submissions Question

Total Accepted: 59147 Total Submissions: 258553 Difficulty: Medium
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:
  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
  
@author: zeminzhang
"""

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        if len(tokens) == 1: return int(tokens[0])
        oper = {'+','-','*','/'}
        stack = []
        for token in tokens:
            if token not in oper:
                stack.append(int(token))
                continue
            else:
                num1 = stack.pop(); num2 = stack.pop()
                res = 0
                if token == '+': res = 1.0*(num2 + num1)
                elif token == '-': res = 1.0*(num2 - num1)
                elif token == '*': res = 1.0*num1*num2
                else: res = 1.0*num2/num1
                stack.append(int(res))
        return stack[0]