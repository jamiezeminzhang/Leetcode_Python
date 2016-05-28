# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 20:31:38 2016

49. Group Anagrams

Total Accepted: 76769 Total Submissions: 275417 Difficulty: Medium

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
        dic = collections.defaultdict(list)
        res = []
        for idx, word in enumerate(strs):
            dic[''.join(sorted(word))].append(word)
        for key in dic:
            res.append(sorted(dic[key]))
        return res

sol = Solution()
print sol.groupAnagrams(["cab","pug","pei","nay","ron","rae","ems","ida","mes"])
