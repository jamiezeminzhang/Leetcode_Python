# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 12:01:11 2016

336. Palindrome Pairs

Total Accepted: 307 Total Submissions: 2027 Difficulty: Hard

Given a list of unique words. Find all pairs of distinct indices (i, j) in the given list, so that 
the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.

Example 1:
Given words = ["bat", "tab", "cat"]
Return [[0, 1], [1, 0]]
The palindromes are ["battab", "tabbat"]
Example 2:
Given words = ["abcd", "dcba", "lls", "s", "sssll"]
Return [[0, 1], [1, 0], [3, 2], [2, 4]]
The palindromes are ["dcbaabcd", "abcddcba", "slls", "llssssll"]

*** 遇到brute force这种穷举会失效，并且明显没有什么快捷算法的题：
1. 特殊数据结构，比如trie， fenwick tree， segment tree
2. 使用dic，使得查找更快。

下题的基本想法：拆分每一个词，查找是否有能使其左右加上某个词变成panlindrome的词在dic中。
时间复杂度O(nk^2)

@author: Jamie

"""

class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        res = []
        dic = {}
        for idx, word in enumerate(words):
            dic[word] = idx
        
        for i, word in enumerate(words):
            for j in range(len(word)+1):
                temp1 = word[:j]
                temp2 = word[j:]
                # includes the case when temp2 == 0
                if temp1[::-1] in dic and i!=dic[temp1[::-1]] and temp2 == temp2[::-1]:
                    res.append([i, dic[temp1[::-1]]])
                if j!=0 and temp2[::-1] in dic and temp1 == temp1[::-1]:
                    res.append([dic[temp2[::-1]] , i])
        return res