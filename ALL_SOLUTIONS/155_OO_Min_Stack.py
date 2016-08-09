# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 03:17:48 2016

155. Min Stack My Submissions Question

Total Accepted: 61120 Total Submissions: 284760 Difficulty: Easy
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.


@author: zeminzhang
"""

class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        curMin = self.getMin()
        if curMin==None or x<curMin: curMin = x
        self.stack.append((x,curMin))

    def pop(self):
        """
        :rtype: nothing
        """
        self.stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        if self.stack: return self.stack[-1][0]
        else: return None

    def getMin(self):
        """
        :rtype: int
        """
        if self.stack: return self.stack[-1][1]
        else: return None        