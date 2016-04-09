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

class Solution:
    # @param {integer} num
    # @return {string}
    def intToRoman(self, num):
        D = {}
        num_str = str(num)
        D[0] = ""
        D[1] = "I" ; D[2] = "II" ; D[3] = "III" ; D[4] = "IV" ; D[5] =  "V"
        D[6] = "VI"; D[7] = "VII"; D[8] = "VIII"; D[9] = "IX"
        D[10] = "X"; D[50] = "L" ; D[100] = "C" ; D[500] = "D"; D[1000] = "M"
        
        if num>=11 and num<= 39:
            return int(num_str[0])*D[10] + D[int(num_str[1])]
        if num>=40 and num <=49:
            return "XL" + D[int(num_str[1])]
        if num >=51 and num<=89:
            return  D[50] + self.intToRoman(num-50)
        if num >=90 and num <= 99:
            return "XC" + D[int(num_str[1])]
        if num >= 101 and num <=399:
            return int(num_str[0])*D[100] + self.intToRoman(int(num_str[1:]))
        if num >=400 and num <= 499:
            return "CD" + self.intToRoman(num-400)
        if num >= 501 and num <= 899:
            return D[500] + self.intToRoman(num-500)
        if num >= 900 and num <= 999:
            return "CM" + self.intToRoman(num-900)
        if num >= 1001:
            return int(num_str[0])*D[1000] + self.intToRoman(int(num_str[1:]))
        
        return D[num]
        
        
        
        
sol = Solution()

print sol.intToRoman(900)