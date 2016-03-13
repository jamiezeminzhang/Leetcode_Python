# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 16:01:54 2016

225. Implement Stack using Queues My Submissions Question
Total Accepted: 31381 Total Submissions: 103181 Difficulty: Easy
Implement the following operations of a stack using queues.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.
Notes:
You must use only standard operations of a queue -- which means only push to back, peek/pop from front, 
size, and is empty operations are valid.
Depending on your language, queue may not be supported natively. You may simulate a queue by using 
a list or deque (double-ended queue), as long as you use only standard operations of a queue.
You may assume that all operations are valid (for example, no pop or top operations will be called 
on an empty stack).

Stack: LIFO
Queue: FIFO
@author: Jamie
"""

class Stack(object):
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
        self.stack += x,
        

    def pop(self):
        """
        :rtype: nothing
        """
        del self.stack[-1]

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.stack) == 0
        