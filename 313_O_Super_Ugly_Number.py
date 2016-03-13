# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 14:27:08 2016

313. Super Ugly Number My Submissions Question
Total Accepted: 8483 Total Submissions: 26350 Difficulty: Medium
Write a program to find the nth super ugly number.

Super ugly numbers are positive numbers whose all prime factors are in the given prime list primes of size k. For example, [1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28, 32] is the sequence of the first 12 super ugly numbers given primes = [2, 7, 13, 19] of size 4.

Note:
(1) 1 is a super ugly number for any given primes.
(2) The given numbers in primes are in ascending order.
(3) 0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000.


Exactly the same with 264 Ugly number

@author: zzhang04
"""

class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        length = len(primes)
        q = [1]
        idx = [0 for x in range(length)]
        
        
        while len(q)<n:
            tmp = [ primes[i] * q[idx[i]] for i in range(length) ]
            m = min(tmp)
            for i in range(len(tmp)):
                if tmp[i] == m: idx[i] += 1
            q.append(m)
        #print q
        return q[-1]