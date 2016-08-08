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

用一个minstack来存储最小值。很巧妙。

@author: zeminzhang
"""

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minstack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if not self.minstack or self.minstack[-1]>=x:
            self.minstack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        if self.stack[-1] == self.minstack[-1]:
            self.minstack.pop()
        self.stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minstack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
        