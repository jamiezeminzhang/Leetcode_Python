# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 16:24:25 2015

LeetCode #21 Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

"((()))", "(()())", "(())()", "()(())", "()()()" 

@author: zzhang

A better solution:
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
"""

class Solution:
    # @param {integer} n
    # @return {string[]}
    def generateParenthesis(self, n):
        if n == 1:
            return ["()"]
            
        if n>=2:
            res_set = set()
            res_pre = self.generateParenthesis(n-1)
            for i in res_pre:
                numLen = len(i)
                maskLen = 2*numLen+1
                mask = "*"*maskLen
                for j in range(1,maskLen,2):
                    mask_temp1 = list(mask)
                    mask_temp1[j] = i[j/2]
                    mask = "".join(mask_temp1)
                mask = "*" + mask + "*"
                for i in range(0,len(mask)-1):
                    for j in range(i+1,len(mask)):
                        if mask[i]=='*' and mask[j]=='*':
                            mask_temp2 = list(mask)
                            mask_temp2[i]='('
                            mask_temp2[j]=')'
                            mask_temp3 = "".join(mask_temp2)
                            mask_wo = mask_temp3.translate(None,"*")                         
                            res_set.add(mask_wo)
        res = list(i for i in res_set)
        return res


sol = Solution()
print sol.generateParenthesis(3)