# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 10:03:31 2016

319. Bulb Switcher

Total Accepted: 11519 Total Submissions: 29153 Difficulty: Medium

There are n bulbs that are initially off. You first turn on all the bulbs. 
Then, you turn off every second bulb. On the third round, you toggle every third 
bulb (turning on if it's off or turning off if it's on). For the ith round, you 
toggle every i bulb. For the nth round, you only toggle the last bulb. 
Find how many bulbs are on after n rounds.

Example:

Given n = 3. 

At first, the three bulbs are [off, off, off].
After first round, the three bulbs are [on, on, on].
After second round, the three bulbs are [on, off, on].
After third round, the three bulbs are [on, off, off]. 

So you should return 1, because there is only one bulb is on.

对于第i栈灯泡，当i的因子个数为奇数时，最终会保持点亮状态，例如9的因子为1，3，9
而当i的因子个数为偶数时，最终会保持熄灭状态，例如8的因子为：1，2，4，8
当且仅当i为完全平方数时，其因子个数为奇数

数学题，答案等于int(math.sqrt(n))

@author: Jamie
"""

class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0: return 0
        k=1
        while k*(k+2)<n:
            k += 1
        return k