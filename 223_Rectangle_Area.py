# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 13:46:03 2016

223. Rectangle Area My Submissions Question

Total Accepted: 30327 Total Submissions: 104121 Difficulty: Easy
Find the total area covered by two rectilinear rectangles in a 2D plane.

Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.

Rectangle Area
Assume that the total area is never beyond the maximum possible value of int.

@author: Jamie
"""

class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        return (C-A)*(D-B) + (G-E)*(H-F) - \
        max(0,(min(C,G) - max(A,E))) * max(0, (min(D,H)-max(B,F)))