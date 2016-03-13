# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 09:50:12 2016

232. Implement Queue using Stacks My Submissions Question

Total Accepted: 33976 Total Submissions: 100193 Difficulty: Easy
Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.
Notes:
You must use only standard operations of a stack -- which means only push to top, peek/pop from top, 
size, and is empty operations are valid.

@author: Jamie
"""

class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.queue = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.queue += x,

    def pop(self):
        """
        :rtype: nothing
        """
        del self.queue[0]
        

    def peek(self):
        """
        :rtype: int
        """
        return self.queue[0]

    def empty(self):
        """
        :rtype: bool
        """
        return not self.queue