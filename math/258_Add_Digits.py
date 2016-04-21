# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 10:06:02 2016

258. Add Digits

Total Accepted: 70293 Total Submissions: 146212 Difficulty: Easy

Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

For example:

Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.

Follow up:
Could you do it without any loop/recursion in O(1) runtime?

Hint:

A naive implementation of the above process is trivial. Could you come up with other methods?
What are all the possible results?
How do they occur, periodically or randomly?
You may find this Wikipedia article useful.

*** digit root （树根） ***
没啥好考的。。。如果知道数学就是一行
https://en.wikipedia.org/wiki/Digital_root

否则就模拟法写也没什么。。。

@author: Jamie
"""


class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        return num-9*((num-1)/9) if num >0 else 0   