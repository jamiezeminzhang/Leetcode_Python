# -*- coding: utf-8 -*-
"""
308. Range Sum Query 2D - Mutable

Total Accepted: 4742
Total Submissions: 22470
Difficulty: Hard

Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

Range Sum Query 2D
The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2, col2) = (4, 3), which contains sum = 8.

Example:
Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
update(3, 2, 2)
sumRegion(2, 1, 4, 3) -> 10
Note:
The matrix is only modifiable by the update function.
You may assume the number of calls to update and sumRegion function is distributed evenly.
You may assume that row1 ≤ row2 and col1 ≤ col2.
@author: Jamie
"""

class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        self.m = matrix
        self.rows = len(self.m)
        if self.rows:
            self.cols = len(self.m[0])
        else:
            self.cols = 0
        
        # construct a Accumulation map 
        cache = [[0]*(self.cols+1) for _ in xrange(self.rows+1)]
        for r in xrange(1,self.rows+1):
            for c in xrange(1,self.cols+1):
                cache[r][c] = matrix[r-1][c-1] + cache[r-1][c] + cache[r][c-1] - cache[r-1][c-1]
    
    
        # then construct two BITs
        self.cache = [[0]*(self.cols+1) for _ in xrange(self.rows+1)]
        for c in xrange(1, self.cols+1):
            for r in xrange(1, self.rows+1):
                last_r = r - (r&(-r))
                last_c = c - (c&(-c))
                self.cache[r][c] = cache[r][c] - cache[r][last_c] - cache[last_r][c]+ cache[last_r][last_c]
        
    def find(self, row, col):
        """
        sum of elements matrix[(0,0)..(row,col)], inclusive.
        :type row: int
        :type col: int
        :rtype: int
        """
        row, col  = row + 1, col + 1
        # BIT index start with 1, LOL
        rval = 0
        while col:
            r = row
            while r:
                rval += self.cache[r][col]
                r -= r&(-r)
            col -= col&(-col)
        return rval
    
    def update(self, row, col, val):
        """
        update the element at matrix[row,col] to val.
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        diff, self.m[row][col] = val - self.m[row][col], val
    
        row, col  = row + 1, col + 1
        while col <= self.cols:
            r = row
            while r <= self.rows:
                self.cache[r][col] += diff
                r += r&(-r)
            col += col&(-col)
    
    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.find(row2, col2)-self.find(row2, col1-1)-self.find(row1-1, col2)+self.find(row1-1, col1-1)