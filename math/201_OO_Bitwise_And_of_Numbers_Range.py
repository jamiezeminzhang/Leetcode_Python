# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 08:47:31 2016

201. Bitwise AND of Numbers Range 

Total Accepted: 28665 Total Submissions: 98213 Difficulty: Medium

Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

For example, given the range [5, 7], you should return 4.


我们再来看一个范围[26, 30]，它们的二进制如下：

11010　　11011　　11100　　11101　　11110

发现了规律后，我们只要写代码找到左边公共的部分即可

@author: Jamie
"""

class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        d = 2**31-1
        while ( m&d ) != (n&d):
            d = d << 1
        return (m&d)