# -*- coding: utf-8 -*-
"""
Created on Friday July 8 09:31:29 2016

371. Sum of Two Integers

Total Accepted: 9172
Total Submissions: 17754
Difficulty: Easy

Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example:
Given a = 1 and b = 2, return 3.

@author: zzhang

*******************************************************************

For this, problem, for example, we have a = 1, b = 3,

In bit representation, a = 0001, b = 0011,

First, we can use "and"("&") operation between a and b to find a carry.

carry = a & b, then carry = 0001

Second, we can use "xor" ("^") operation between a and b to find the different bit, and assign it to a,

Then, we shift carry one position left and assign it to b, b = 0010.

Iterate until there is no carry (or b == 0)

***
actually it can handle negative number.

for example, a = -1 (1111), b = 2 (0010),

i = 0, carry = 0010, a = 1101, b = 0100

i = 1, carry = 0100, a = 1001, b = 1000

i = 2, carry = 1000, a = 0001, b = 0000, stop, return a(1)

***
Of course, Python doesn’t use 8-bit numbers. It USED to use however many bits were native to your machine, but since that was non-portable, it has recently switched to using an INFINITE number of bits. Thus the number -5 is treated by bitwise operators as if it were written “…1111111111111111111011”.

Then we need to make sure a and b are within the right range.

"""

class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s = {-1: set()}
        for x in sorted(nums):
            s[x] = max((s[d] for d in s if x%d==0), key=len) | {x}
        return list(max(s.values(), key=len))