# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 09:25:38 2016

318. Maximum Product of Word Lengths My Submissions Question
Total Accepted: 12859 Total Submissions: 33001 Difficulty: Medium
Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the 
two words do not share common letters. You may assume that each word will contain only lower case 
letters. If no such two words exist, return 0.

Example 1:
Given ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
Return 16
The two words can be "abcw", "xtfn".

Example 2:
Given ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
Return 4
The two words can be "ab", "cd".

Example 3:
Given ["a", "aa", "aaa", "aaaa"]
Return 0
No such pair of words.


解题思路：
max( O(n^2), O(n*m) )解法，其中：n为单词个数，m为单词平均长度：

1. O(n)的预处理，将单词数组words转化为整数数组nums，其中：nums[i] = sum(1 << (ord(x) - ord('a')) for x in set(words[i]))

2. O(n^2)的循环，寻找nums中满足nums[x] & nums[y] == 0的整数对，并计算对应的length(words[i]) * length(words[j])的值

@author: Jamie
"""

class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        nums = []
        num_words = len(words)
        for w in words:
            nums += sum( 1<<(ord(x)-ord('a')) for x in set(w) ),
        
        res = 0
        for idx1, x in enumerate(nums):
            for idx2, y in enumerate(nums):
                if x & y == 0:
                    res = max(res, len(words[idx1])*len(words[idx2]) )
        return res