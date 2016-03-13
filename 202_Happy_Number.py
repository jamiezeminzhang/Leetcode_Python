# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 08:58:57 2016

202. Happy Number My Submissions Question
Total Accepted: 54462 Total Submissions: 153037 Difficulty: Easy
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, 
replace the number by the sum of the squares of its digits, and repeat the process until the number 
equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. 
Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number

12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

模拟题，循环过程中用set记录每次得到的平方和

当出现非1的重复平方和时，返回False

否则，返回True

我自己的答案是错的实际上。。。

@author: Jamie
"""

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        max_loop = 100
        loop = 0
        while loop < max_loop:
            s = str(n)
            n = 0
            for i in range(len(s)):
                n += int(s[i])**2
            if n == 1: return True
            loop += 1
        return False