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
        if not matrix: return
        self.m, self.n = len(matrix), len(matrix[0])
        self.matrix = matrix
        self.sums = [[0]*(self.n+1) for _ in range(self.m+1)]
        for i in range(self.m):
            for j in range(self.n):
                self.add(i+1, j+1, self.matrix[i][j])
    
    def add(self, row, col, val):
        i = row
        while i<=self.m:
            j = col
            while j<=self.n:
                self.sums[i][j] += val
                j += (j&-j)
            i += (i&-i)
                
        
    def update(self, row, col, val):
        """
        update the element at matrix[row,col] to val.
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        self.add(row+1, col+1, val-self.matrix[row][col])
        self.matrix[row][col] = val
    
    def getsum(self, row, col):
        ans = 0
        i= row
        while i>0:
            j = col
            while j>0:
                ans += self.sums[i][j]
                j -= (j&-j)
            i -= (i&-i)
        return ans
        

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.getsum(row2+1, col2+1) + self.getsum(row1, col1) - \
        self.getsum(row1, col2+1) - self.getsum(row2+1, col1)

# Your NumMatrix object will be instantiated and called as such:
# numMatrix = NumMatrix(matrix)
# numMatrix.sumRegion(0, 1, 2, 3)
# numMatrix.update(1, 1, 10)
# numMatrix.sumRegion(1, 2, 3, 4)
