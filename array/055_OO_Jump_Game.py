# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 21:02:15 2016

55. Jump Game

Total Accepted: 76927 Total Submissions: 272495 Difficulty: Medium

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.

@author: zeminzhang
"""

class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        step = A[0]
        for i in range(1, len(A)):
            if step > 0: # step: how many steps left we could walk. if it's 0 then we have to stop
                step -= 1 # you make one move, you have 1 less step
                step = max(step, A[i])
            else:
                return False
        return True
