# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 05:49:06 2016

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?


@author: zeminzhang
"""

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1: return 1
        res = 0
        for y in range(n/2+1):
            x = n - y*2
            # now compute C_{x+y}^{x}
            if x==0 or y == 0:
                res += 1
            else:
                num1 = 1
                num2 = 1
                for i in range(x+y,y,-1):
                    num1 *= i
                for j in range(x,0,-1):
                    num2 *= j 
                res += num1/num2
        return res