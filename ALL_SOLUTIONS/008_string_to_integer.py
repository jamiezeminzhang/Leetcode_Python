# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 14:57:30 2015

LeetCode #8 String to Integer

Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. 
If you want a challenge, please do not see below and ask yourself what are the 
possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given 
input specs). 
You are responsible to gather all the input requirements up front.


Requirements for atoi:

The function first discards as many whitespace characters as necessary until
 the first non-whitespace character is found. Then, starting from this 
 character, takes an optional initial plus or minus sign followed by as many 
 numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the 
integral number, which are ignored and have no effect on the behavior of 
this function.

If the first sequence of non-whitespace characters in str is not a valid 
integral number, or if no such sequence exists because either str is empty 
or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned. 
If the correct value is out of the range of representable values, 
INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.


@author: zzhang
"""

class Solution:
    # @param {string} str
    # @return {integer}
    def myAtoi(self, str):
        if str == "":
            return 0
        else:
            INT_MAX = 2**31 - 1
            INT_MIN = -2**31 

            integer = ["0","1","2","3","4","5","6","7","8","9"]
            result = ""
            # remove space at the beginning
            i_space = 0
            while i_space < len(str):
                if str[i_space] != " ":
                    str = str[i_space:]
                    break
                i_space += 1
                
            # check sign
            if str[0] == "-":
                sign = -1
                str = str[1:]
            elif str[0] == "+":
                sign = 1
                str = str[1:]
            else:
                sign = 1
            
            
            for idx,i in enumerate(str):
                if i not in integer and idx == 0:
                    return 0
                elif i not in integer and idx !=0:
                    break
                else:
                    result += i
            
            num = sign*int(result)
  
            if num> INT_MAX:
                return INT_MAX
            elif num < INT_MIN:
                return INT_MIN
            else:
                return num
