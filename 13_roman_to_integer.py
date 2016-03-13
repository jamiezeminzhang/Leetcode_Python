# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 14:36:15 2015

LeetCode #13 Roman to Integer

Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.

@author: zzhang
"""

class Solution:
    # @param {string} s
    # @return {integer}
    def romanToInt(self, s):
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        if len(s) == 0 :
            return 0
        if len(s) == 1:
            return roman[s]
        
        num = 0
        for idx, i in enumerate(s):
            if  idx < len(s)-1:
                if roman[i] >= roman[s[idx+1]]:
                    num += roman[i]
                else:
                    num -= roman[i]
            elif idx == len(s)-1:
                num += roman[i]
            
        return num


sol = Solution()

print sol.romanToInt("XCVI")