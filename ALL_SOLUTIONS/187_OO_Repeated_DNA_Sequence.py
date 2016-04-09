# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 06:10:03 2016

187. Repeated DNA Sequences My Submissions Question
Total Accepted: 37005 Total Submissions: 154531 Difficulty: Medium
All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: 
"ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

For example,

Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",

Return:
["AAAAACCCCC", "CCCCCAAAAA"].

解题思路：
字典+位运算，或者进制转换。

由于直接将字符串存入字典会导致Memory Limit Exceeded，采用位操作将字符串转化为整数可以减少内存开销。

class Solution:
    # @param s, a string
    # @return a list of strings
    def findRepeatedDnaSequences(self, s):
        ans = []
        valCnt = dict()
        map = {'A' : 0, 'C' : 1, 'G': 2, 'T' : 3}
        sum = 0
        for x in range(len(s)):
            sum = (sum * 4 + map[s[x]]) & 0xFFFFF
            if x < 9:
                continue
            valCnt[sum] = valCnt.get(sum, 0) + 1
            if valCnt[sum] == 2:
                ans.append(s[x - 9 : x + 1])
        return ans
        

0xFFFFF = pow(4, 10)，按位与0xFFFFF是为了确保只记录10位碱基。


*** Get familiar with dict.get(key, default = None)
@author: Jamie
"""
class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        dic = dict(); res=set()
        for i in range(len(s)-9):
            ss = s[i:i+10]
            dic[ss] = dic.get(ss,0) + 1
            if dic[ss]>=2:
                res.add(ss)
        return list(res)
