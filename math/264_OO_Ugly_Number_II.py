# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 13:26:43 2016

264. Ugly Number II

Total Accepted: 23373 Total Submissions: 88040 Difficulty: Medium

Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 
1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.

Note that 1 is typically treated as an ugly number.

Hint:

The naive approach is to call isUgly for every number until you reach the nth one. Most numbers
are not ugly. Try to focus your effort on generating only the ugly ones.
An ugly number must be multiplied by either 2, 3, or 5 from a smaller ugly number.
The key is how to maintain the order of the ugly numbers. Try a similar approach of merging from
 three sorted lists: L1, L2, and L3.
Assume you have Uk, the kth ugly number. Then Uk+1 must be Min(L1 * 2, L2 * 3, L3 * 5).

解题思路：
参考：http://www.geeksforgeeks.org/ugly-numbers/

丑陋数序列可以拆分为下面3个子列表：

(1) 1×2, 2×2, 3×2, 4×2, 5×2, …
(2) 1×3, 2×3, 3×3, 4×3, 5×3, …
(3) 1×5, 2×5, 3×5, 4×5, 5×5, …
我们可以发现每一个子列表都是丑陋数本身(1, 2, 3, 4, 5, …) 乘以 2, 3, 5

接下来我们使用与归并排序相似的合并方法，从3个子列表中获取丑陋数。每一步我们从中选出最小的一个，然后向后移动一步。

@author: Jamie
"""

class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        q = [1]
        i2, i3, i5 = 0,0,0
        while len(q)<n:
            m2, m3, m5 = q[i2]*2, q[i3]*3, q[i5]*5
            m = min(m2,m3,m5)
            i2 += 1 if m == m2 else 0
            i3 += 1 if m == m3 else 0
            i5 += 1 if m == m5 else 0
            q.append(m)
        return q[-1]