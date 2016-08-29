# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 08:42:10 2016

166. Fraction to Recurring Decimal 

Total Accepted: 26284 Total Submissions: 180852 Difficulty: Medium

Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

For example,

Given numerator = 1, denominator = 2, return "0.5".
Given numerator = 2, denominator = 1, return "2".
Given numerator = 2, denominator = 3, return "0.(6)".

@author: Jamie
"""

class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator == 0: return '0'
        sign = '-' if numerator*denominator<0 else ''
        numerator, denominator = abs(numerator), abs(denominator)
        ans = sign+str(numerator/denominator)
        numerator = numerator - abs(int(ans))*denominator
        
        repeated, num_save = [], [numerator]
        while numerator !=0:
            numerator *= 10
            div = str(numerator/denominator)
            numerator = numerator - int(div)*denominator
            repeated.append(div)
            if numerator in num_save:
                idx = num_save.index(numerator)
                repeated.insert(idx,'(')
                repeated.append(')')
                break
            num_save.append(numerator)
        if len(repeated) != 0:
            ans = ans + '.' + ''.join(repeated)
        return ans
        