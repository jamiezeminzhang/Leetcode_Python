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
        self.stack1 = [] # normal stack
        self.stack2 = [] # for retrieving min

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.stack1.append(x)
        if (not self.stack2) or (x<=self.stack2[-1]):
            self.stack2.append(x)
        

    def pop(self):
        """
        :rtype: nothing
        """
        value1 = self.stack1.pop()
        if value1 == self.stack2[-1]:
            self.stack2.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack1[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack2[-1]
        