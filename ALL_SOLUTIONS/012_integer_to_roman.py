# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 13:44:48 2015

LeetCode #12 Integer to Roman

Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.

@author: zzhang
"""

"""
Better solution

class Solution:
    # @return a string
    def intToRoman(self, num):
        values = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
        numerals = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
        list = ''
        for i in range(0, len(values)):
            while num >= values[i]:
                num -= values[i]
                list += numerals[i]
        return list
    

"""

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        M = ['','M','MM','MMM']
        C = ['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM']
        X = ['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC']
        I = ['','I','II','III','IV','V','VI','VII','VIII','IX']
        return M[num/1000]+C[(num%1000)/100]+X[(num%100)/10]+I[num%10]
