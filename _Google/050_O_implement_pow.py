# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 20:49:29 2016

50. Pow(x, n)

Total Accepted: 92719 Total Submissions: 332083 Difficulty: Medium

Implement pow(x, n).

解题思路：求幂函数的实现。使用递归，类似于二分的思路，解法来自Mark Allen Weiss的《数据结构与算法分析》。

@author: zeminzhang
"""

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n==0: return 1.0
        if n<0: return 1.0/self.myPow(x,-n)
        if n%2: return self.myPow(x*x,n/2)*x
        else: return self.myPow(x*x,n/2)
        
