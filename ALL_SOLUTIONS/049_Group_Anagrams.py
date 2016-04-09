# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 20:31:38 2016

Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"], 
Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:
For the return value, each inner list's elements must follow the lexicographic order.
All inputs will be in lower-case.

@author: zeminzhang
"""

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dict = {}
        for word in strs:
            tmp = []
            for i in word:
                tmp.append(i)
            tmp.sort()
            tmp = tuple(tmp)
            
            if tmp not in dict:
                dict[tmp] = []
                dict[tmp].append(word)
            else:
                dict[tmp].append(word)
        
        res = []
        for tmp2 in dict:
            dict[tmp2].sort()
            res.append(dict[tmp2])
        
        return res

sol = Solution()
print sol.groupAnagrams(["cab","pug","pei","nay","ron","rae","ems","ida","mes"])