# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 02:17:44 2016

Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [−2,1,−3,4,−1,2,1,−5,4],
the contiguous subarray [4,−1,2,1] has the largest sum = 6.


@author: zeminzhang
"""

class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        ThisSum = 0
        MaxSum = -100000000
        
        for i in range( 0, len(A) ):
            if ThisSum < 0:   #如果之前的比0小，直接放弃选择下一个，无论都大都比加之前的大
                ThisSum = 0
            ThisSum = ThisSum + A[i]
            MaxSum = max( ThisSum, MaxSum )

        return MaxSum