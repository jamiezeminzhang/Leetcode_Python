# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 09:40:32 2016

171. Excel Sheet Column Number 

Total Accepted: 64630 Total Submissions: 160845 Difficulty: Easy

Related to question Excel Sheet Column Title

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    
@author: Jamie
"""

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {'A':1,'B':2,'C':3,'D':4,'E':5,\
        'F':6,'G':7,'H':8,'I':9,'J':10,\
        'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,\
        'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}
        ans = 0
        s_reverse = s[::-1]
        for i in range(len(s_reverse)):
            ans += dic[ s_reverse[i] ] * 26**i
        
        return ans