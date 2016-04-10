# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 09:25:32 2016

168. Excel Sheet Column Title

Total Accepted: 51647 Total Submissions: 249119 Difficulty: Easy

Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
    
@author: Jamie
"""

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        table = ['#','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S',\
        'T','U','V','W','X','Y','Z']
        res = []
        ans = ''
        while n>26:
            d = (n-1)/26
            res.append(n-26*d)
            n = d
        res.append(n)
        res.reverse()
        return ''.join(map(lambda x:table[x], res))

sol = Solution()
print sol.convertToTitle(703)