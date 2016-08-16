# -*- coding: utf-8 -*-
"""
2016/08/11 08:56 PST

281. Zigzag Iterator

Total Accepted: 12224
Total Submissions: 27176
Difficulty: Medium

Given two 1d vectors, implement an iterator to return their elements alternately.

For example, given two 1d vectors:

v1 = [1, 2]
v2 = [3, 4, 5, 6]
By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1, 3, 2, 4, 5, 6].

Follow up: What if you are given k 1d vectors? How well can your code be extended to such cases?

Clarification for the follow up question - Update (2015-09-18):
The "Zigzag" order is not clearly defined and is ambiguous for k > 2 cases. If "Zigzag" does not look right to you, replace "Zigzag" with "Cyclic". For example, given the following input:

[1,2,3]
[4,5,6,7]
[8,9]
It should return [1,4,8,2,5,9,3,6,7].

@author: zzhang
"""

class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        cache = [v1[::-1], v2[::-1]]
        self.list_all = [i for i in cache if i]
        self.cur = 0
        
    def next(self):
        """
        :rtype: int
        """
        if self.cur == -1 or not self.list_all: return False

        next_val = self.list_all[self.cur].pop()
        if self.list_all[self.cur]:
            self.cur = self.cur+1 if self.cur < len(self.list_all)-1 else 0
        else:
            while self.cur<len(self.list_all) and not self.list_all[self.cur]:
                self.list_all.pop(self.cur)
            if self.cur == len(self.list_all):
                if self.list_all and self.list_all[0]:
                    self.cur = 0
                else:
                    self.cur = -1
        return next_val
            
        

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.cur == -1 or not self.list_all: return False
        return True
        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())