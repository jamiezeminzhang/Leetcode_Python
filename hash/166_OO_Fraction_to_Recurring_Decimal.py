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

解题的关键是当余数开始循环时，得数也会开始循环。

你需要用一个哈希表存储：key = 余数， value = 当前数位在小数得数中的位置。一旦找到重复的余数，
就可以通过查找哈希表获得循环节的起点，从而得到小数的循环节。

执行除法的过程中，余数可能变为0。此时说明小数是有限小数，可以立即返回得数。

与问题Divide Two Integers类似，需要注意负数和极限情况，例如-2147483648 / -1

@author: Jamie
"""

class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        negative_flag = numerator*denominator < 0
        numerator, denominator = abs(numerator), abs(denominator)
        
        num_list = []
        cnt = 0
        loopDict = {}
        loopStr = ''
        
        while True:
            num_list.append(str(numerator/denominator))
            cnt += 1
            numerator = 10*(numerator % denominator)
            if numerator == 0:
                break
            loc = loopDict.get(str(numerator))
            if loc:
                loopStr = ''.join(num_list[loc:cnt])
                break
            loopDict[str(numerator)] = cnt
        ans = num_list[0]
        if len(num_list) > 1: ans += '.'
        if not loopStr:
            ans += ''.join(num_list[1:])
        else:
            ans += ''.join(num_list[1:loc]) + '(' + loopStr + ')'
        if negative_flag:
            ans = '-'+ans
        return ans
        
sol = Solution()
print sol.fractionToDecimal(1,5)