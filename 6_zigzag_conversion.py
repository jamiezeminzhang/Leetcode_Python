# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 12:02:32 2015

LeetCode #6: ZigZag Conversion

 The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 
 (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);

convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR". 

"""

class Solution:
    # @param {string} s
    # @param {integer} numRows
    # @return {string}
    def convert(self, s, numRows):
        if s == None or len(s) == 0 or numRows ==0:
            return ""
        elif numRows == 1:
            return s
        
        result = ""        
        K = 2*numRows-2
        
        for i in range(numRows):
            j = i
            while j < len(s):
                result = result + s[j]
                j = j+K
                if i != 0 and i!=(numRows-1) and (j-2*i) < len(s):
                    result = result + s[j-2*i]
        
        return result