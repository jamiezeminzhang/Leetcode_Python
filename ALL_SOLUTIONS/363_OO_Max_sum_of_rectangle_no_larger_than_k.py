# -*- coding: utf-8 -*-
"""
Created on Thu June 29 09:42:57 2016

363. Max Sum of Rectangle No Larger Than K 

Total Accepted: 830 Total Submissions: 3103 Difficulty: Hard

Given a non-empty 2D matrix matrix and an integer k, find the max sum of a rectangle in the matrix such that its sum is no larger than k.

Example:
Given matrix = [
  [1,  0, 1],
  [0, -2, 3]
]
k = 2
The answer is 2. Because the sum of rectangle [[0, 1], [-2, 3]] is 2 and 2 is the max number no larger than k (k = 2).

Note:
The rectangle inside the matrix must have an area > 0.
What if the number of rows is much larger than the number of columns?

@author: zzhang
"""

class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        m, n = len(matrix), len(matrix[0])
        M, N, ans = max(m, n), min(m, n), None
        for x in range(N):
            sums = [0] * M
            for y in range(x, N):
                slist, num = [], 0
                for z in range(M):
                    sums[z] += matrix[z][y] if m > n else matrix[y][z]
                    num += sums[z]
                    if num <= k: ans = max(ans, num)
                    i = bisect.bisect_left(slist, num - k)
                    if i != len(slist): ans = max(ans, num - slist[i])
                    bisect.insort(slist, num)
        return ans