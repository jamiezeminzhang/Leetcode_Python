# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 13:44:34 2016

335. Self Crossing

Total Accepted: 1190 Total Submissions: 6642 Difficulty: Medium

You are given an array x of n positive numbers. You start at point (0,0) and moves x[0] metres 
to the north, then x[1] metres to the west, x[2] metres to the south, x[3] metres to the east and so on. 
In other words, after each move your direction changes counter-clockwise.

Write a one-pass algorithm with O(1) extra space to determine, if your path crosses itself, or not.

Example 1:
Given x = [2, 1, 1, 2],
┌───┐
│   │
└───┼──>
    │

Return true (self crossing)
Example 2:
Given x = [1, 2, 3, 4],
┌──────┐
│      │
│
│
└────────────>

Return false (not self crossing)
Example 3:
Given x = [1, 1, 1, 1],
┌───┐
│   │
└───┼>

Return true (self crossing)

*****
Explanation

            b                              b
   +----------------+             +----------------+
   |                |             |                |
   |                |             |                | a
 c |                |           c |                |
   |                | a           |                |    f
   +----------->    |             |                | <----+
            d       |             |                |      | e
                    |             |                       |
                                  +-----------------------+
                                               d
Draw a line of length a. Then draw further lines of lengths b, c, etc. How does the a-line get crossed? 
From the left by the d-line or from the right by the f-line, see the above picture. 
I just encoded the criteria for actually crossing it.

Two details:

In both cases, d needs to be at least b. In the first case to cross the a-line directly, and in the 
second case to get behind it so that the f-line can cross it. So I factored out d >= b.
The "special case" of the e-line stabbing the a-line from below is covered because in that case, the 
f-line "crosses" it (note that even if there is no actual f-line, my code uses f = 0 and thus still 
finds that "crossing").

事实上，每次循环，我们每次都把上面的方框右转90度。
所以上次的a是现在的b，上次的b是现在的c，上次的c是现在的d。。。

而实际上正确的方向是这个
            c                              e
   +----------------+             +----------------+
   |                |             |                |
   |                |             |                | f
 b |                |           d |                |
   |                | d           |                |    a
   +----------->    |             |                | <----+
            a       |             |                |      | b
                    |             |                       |
                                  +-----------------------+
                                               c
											   


@author: Jamie
"""

class Solution(object):
    def isSelfCrossing(self, x):
        """
        :type x: List[int]
        :rtype: bool
        """
        b,c,d,e = 0,0,0,0
        for a in x:
            if d>=b > 0 and (a>=c or a>=c-e>0 and f>=d-b):
                return True
            b,c,d,e,f = a,b,c,d,e
        return False