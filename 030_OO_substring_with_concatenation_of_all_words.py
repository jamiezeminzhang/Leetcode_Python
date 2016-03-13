# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 13:34:41 2015

LeetCode # 28: Substring with Concatenation of All Words

 You are given a string, s, and a list of words, words, that are all of the
 same length. Find all starting indices of substring(s) in s that is a 
 concatenation of each word in words exactly once and without any intervening characters.

For example, given:
s: "barfoothefoobarman"
words: ["foo", "bar"]

You should return the indices: [0,9].
(order does not matter). 

@author: zzhang
"""

class Solution:
    # @param {string} s
    # @param {string[]} words
    # @return {integer[]}
    def findSubstring(self, s, words):
        word = {}
        wordNum = len(words)
        wordLen = len(words[0])
        
        for i in words:
            if i not in word:
                word[i] = 1
            else:
                word[i]+=1
                
        res = []
        for i in range(len(s)+1-wordLen*wordNum):
            curr={}
            j = 0
            while j < wordNum:
                w = s[i+j*wordLen:i+j*wordLen+wordLen]
                if w not in words:
                    break
                if w not in curr:
                    curr[w] = 1
                else:
                    curr[w]+= 1
                if curr[w]>word[w]: break
                j += 1
            if j == wordNum: res.append(i)
        return res
        