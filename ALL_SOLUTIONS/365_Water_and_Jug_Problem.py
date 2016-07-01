# -*- coding: utf-8 -*-
"""
Created on Friday July 1 09:19:07 2016

365. Water and Jug Problem

Total Accepted: 1597 Total Submissions: 7911 Difficulty: Medium

You are given two jugs with capacities x and y litres. There is an infinite amount of water supply available. You need to determine whether it is possible to measure exactly z litres using these two jugs.

If z liters of water is measurable, you must have z liters of water contained within one or both buckets by the end.

Operations allowed:

Fill any of the jugs completely with water.
Empty any of the jugs.
Pour water from one jug into another till the other jug is completely full or the first jug itself is empty.
Example 1: (From the famous "Die Hard" example)

Input: x = 3, y = 5, z = 4
Output: True
Example 2:

Input: x = 2, y = 6, z = 5
Output: False

@author: zzhang
"""

import fractions
class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        if z==0: return True
        if x==0: return y==z
        if y==0: return x==z
        g = fractions.gcd(x,y)
        if g==1: return True if x+y>=z else False
        else: return True if z%g==0 and x+y>=z else False