# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 16:24:25 2015

LeetCode #21 Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

"((()))", "(()())", "(())()", "()(())", "()()()" 

@author: zzhang

"""

class Solution:
    # @param an integer
    # @return a list of string
    # @draw a decision tree when n == 2, and you can understand it!
    def helpler(self, l, r, item, res):
        if r < l:
            return
        if l == 0 and r == 0:
            res.append(item)
        if l > 0:
            self.helpler(l - 1, r, item + '(', res)
        if r > 0:
            self.helpler(l, r - 1, item + ')', res)
    
    def generateParenthesis(self, n):
        if n == 0:
            return []
        res = []
        self.helpler(n, n, '', res)
        return res


sol = Solution()
print sol.generateParenthesis(3)