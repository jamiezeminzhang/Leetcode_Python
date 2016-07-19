# -*- coding: utf-8 -*-
"""
Created on Tuesday July 19 09:04:12 2016

374. Guess Number Higher or Lower  

Total Accepted: 6417
Total Submissions: 20270
Difficulty: Easy
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number is higher or lower.

You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):

-1 : My number is lower
 1 : My number is higher
 0 : Congrats! You got it!
Example:
n = 10, I pick 6.

Return 6.

@author: zzhang

"""

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1: return 1
        left, right = 0, n
        while left<=right:
            mid = (left+right)/2
            if guess(mid)==0: return mid
            elif guess(mid)==1: left = mid+1
            else: right = mid-1