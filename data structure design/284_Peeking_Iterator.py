# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 14:17:20 2016

284. Peeking Iterator

Total Accepted: 15198 Total Submissions: 46219 Difficulty: Medium

Given an Iterator class interface with methods: next() and hasNext(), design and implement a 
PeekingIterator that support the peek() operation -- it essentially peek() at the element that 
will be returned by the next call to next().

Here is an example. Assume that the iterator is initialized to the beginning of the list: [1, 2, 3].

Call next() gets you 1, the first element in the list.

Now you call peek() and it returns 2, the next element. Calling next() after that still return 2.

You call next() the final time and it returns 3, the last element. Calling hasNext() after that 
should return false.

Hint:

Think of "looking ahead". You want to cache the next element.
Is one variable sufficient? Why or why not?
Test your design with call order of peek() before next() vs next() before peek().
For a clean implementation, check out Google's guava library source code.
Follow up: How would you extend your design to be generic and work with all types, not just integer?

*** Second time ***
*** I only used one stack to do this ***
class PeekingIterator(object):
    def __init__(self, iterator):
        self.iterator = iterator
        self.peeked = []

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if len(self.peeked) !=0: return self.peeked[0]
        if not self.iterator.hasNext(): return False
        temp = self.iterator.next()
        self.peeked.append(temp)
        return temp
        
    def next(self):
        """
        :rtype: int
        """
        if len(self.peeked) == 0: return self.iterator.next()
        else: return self.peeked.pop(0)

    def hasNext(self):
        """
        :rtype: bool
        """
        if len(self.peeked) !=0: return True
        else: return self.iterator.hasNext()
		
@author: Jamie
"""

# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator(object):
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.hasPeeked = False
        self.PeekedElement = 0
        
    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.hasPeeked:
            return self.PeekedElement
        else:
            if self.iterator.hasNext():
                self.PeekedElement = self.iterator.next()
                self.hasPeeked = True
                return self.PeekedElement
            else:
                self.PeekedElement = None
                return None

    def next(self):
        """
        :rtype: int
        """

        if self.hasPeeked:
            self.hasPeeked = False
            return self.PeekedElement
        else:
            return self.iterator.next()
        

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.hasPeeked:
            return True
        else:
            return self.iterator.hasNext()

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].