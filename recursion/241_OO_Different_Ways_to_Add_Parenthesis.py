# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 09:03:39 2016

241. Different Ways to Add Parentheses

Total Accepted: 16978 Total Submissions: 51564 Difficulty: Medium

Given a string of numbers and operators, return all possible results from computing all the 
different possible ways to group numbers and operators. The valid operators are +, - and *.


Example 1
Input: "2-1-1".

((2-1)-1) = 0
(2-(1-1)) = 2
Output: [0, 2]


Example 2
Input: "2*3-4*5"

(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10
Output: [-34, -14, -10, -10, 10]

*****
learn some definition like this
def calc(a, b, o):
    return {'+':lambda x,y:x+y, '-':lambda x,y:x-y, '*':lambda x,y:x*y}[o](a, b)
    
x = calc(3,4,'+')
x = 7
***

#### Please try to understand what is going on here ###

A simpler version but more lines:

class Solution(object):
    def diffWaysToCompute(self, input):
        ans = []
        for i,c in enumerate(input):
            if c in '+-*':
                for a in self.diffWaysToCompute(input[:i]):
                    for b in self.diffWaysToCompute(input[i+1:]) or [int(input)]:
                        if c=='+': ans+= a+b,
                        elif c=='-': ans+= a-b,
                        else: ans+= a*b,
        return ans or [int(input)]


@author: Jamie
"""

class Solution(object):
    """
    :type input: str
    :rtype: List[int]
    """
    def diffWaysToCompute(self, input):
        return [  a+b if c == '+' else a-b if c == '-' else a*b \
            for i, c in enumerate(input) if c in '+-*'          \
            for a in self.diffWaysToCompute(input[:i])          \
            for b in self.diffWaysToCompute(input[i+1:])  ] or [int(input)]

        