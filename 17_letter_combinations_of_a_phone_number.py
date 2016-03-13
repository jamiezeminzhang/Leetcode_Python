# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 12:25:52 2015

LeetCode #17 Letter Combinations of a Phone Number

Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.

@author: zzhang
"""

class Solution:
    # @param {string} digits
    # @return {string[]}
    def letterCombinations(self, digits):
        D = {
        "2": ["a","b","c"],
        "3": ["d","e","f"],
        "4": ["g","h","i"],
        "5": ["j","k","l"],
        "6": ["m","n","o"],
        "7": ["p","q","r","s"],
        "8": ["t","u","v"],
        "9": ["w","x","y","z"]
        }
        
        
        digits_str = str(digits)
        l = len(digits_str)
        res = []
        
        if l == 0:
            return []
        if l == 1:
            for i in D[digits_str]:
                res.append(i)
            return res
        if l >=2:
            digits1 = digits_str[:(l-1)]
            digits2 = digits_str[l-1]
            
            result1 = self.letterCombinations(digits1)
            for i in result1:
                for j in D[digits2]:
                    ele = i+j
                    res.append(ele)
        
        return res




sol = Solution();
print sol.letterCombinations(23)