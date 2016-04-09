# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 10:57:57 2016

282. Expression Add Operators My Submissions Question
Total Accepted: 7924 Total Submissions: 33827 Difficulty: Hard
Given a string that contains only digits 0-9 and a target value, return all possibilities to add binary operators (not unary) +, -, or * between the digits so they evaluate to the target value.

Examples: 
"123", 6 -> ["1+2+3", "1*2*3"] 
"232", 8 -> ["2*3+2", "2+3*2"]
"105", 5 -> ["1*0+5","10-5"]
"00", 0 -> ["0+0", "0-0", "0*0"]
"3456237490", 9191 -> []

*** My answer didn't consider the case of

"105", 5 -> ["1*0+5","10-5"]

that 105 could be regarded as 10 and 5
should not transcript into stack first

注意：包含前导0的运算数是无效的。

例如，通过"00+9"获得目标值9是不正确的。

@author: zzhang04
"""

class Solution(object):
    def addOperators(self, num, target):
        res, self.target = [], target
        for i in range(1,len(num)+1):
            if i == 1 or (i > 1 and num[0] != "0"): # prevent "00*" as a number
                self.dfs(num[i:], num[:i], int(num[:i]), int(num[:i]), res) # this step put first number in the string
        return res

    def dfs(self, num, temp, cur, last, res):
        if not num:
            if cur == self.target:
                res.append(temp)
            return
        for i in range(1, len(num)+1):
            val = num[:i]
            if i == 1 or (i > 1 and num[0] != "0"): # prevent "00*" as a number
                self.dfs(num[i:], temp + "+" + val, cur+int(val), int(val), res)
                self.dfs(num[i:], temp + "-" + val, cur-int(val), -int(val), res)
                self.dfs(num[i:], temp + "*" + val, cur-last+last*int(val), last*int(val), res)