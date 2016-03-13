# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 20:49:29 2016

Implement pow(x, n).

解题思路：求幂函数的实现。使用递归，类似于二分的思路，解法来自Mark Allen Weiss的《数据结构与算法分析》。

@author: zeminzhang
"""

class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def myPow(self, x, n):
        if n == 0:
            return 1.0
        elif n < 0:
            return 1 / self.myPow(x, -n)
        elif n % 2:
            return self.myPow(x*x,n/2)*x
        else:
            return self.myPow(x*x,n/2)
        
sol = Solution()
print sol.myPow(2,16)