# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 23:15:23 2016

126. Word Ladder II My Submissions Question
Total Accepted: 38701 Total Submissions: 286726 Difficulty: Hard
Given two words (beginWord and endWord), and a dictionary's word list, find 
all shortest transformation sequence(s) from beginWord to endWord, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the word list
For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
Return
  [
    ["hit","hot","dot","dog","cog"],
    ["hit","hot","lot","log","cog"]
  ]

Word Ladder II自己写的一直超时，看了discuss里的这个解法，用defaultdict，很好很强大，佩服佩服！
defaultdict和普通dict的不同就是它允许有默认值，比如d = collections.defaultdict(set),
 即使没有5这个key，d[5]仍然有值，是set([])。如果用int来初始化，d[5]默认值就是0。用list来初始化，
 d[5]默认值就是[]。我根据自己的理解写了一下注释，再次赞Python的简洁。

228ms
@author: zeminzhang
"""
import collections

class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string
    def findLadders(self, start, end, dic):
        # thanks to https://leetcode.com/discuss/24191/defaultdict-for-traceback
        # -and-easy-writing-lines-python-code
        dic.add(end)
        level = set([start])
        # key is word, value is parent word, e.g. {'hot': set(['hit']), 'cog': set(['log', 'dog'])}
        # In each level, defaultdict(set) can remove duplicates, first we need to get parent dictionary
        parents = collections.defaultdict(set)
        while level and end not in parents:
            next_level = collections.defaultdict(set)
            for word in level:
                for char in 'abcdefghijklmnopqrstuvwxyz':
                    for i in xrange(len(start)):
                        childWord = word[:i] + char + word[i+1:]
                        if childWord in dic and childWord not in parents: # 注意这里为什么需要他不在parent里
                            next_level[childWord].add(word)              # 是因为每一轮只算这一轮的level的next和curr
            level = next_level                                           # 否则会 TLE
            parents.update(next_level)
        # then according parent dictionary, build result from end word to start word
        res = [[end]]
        print parents
        while res and res[0][0] != start:
            print res
            res = [ [p] + r for r in res for p in parents[r[0]] ]
        return res
beginWord = "hit"
endWord = "cog"
wordList = {"hot","dot","dog","lot","log"}
sol = Solution()
print sol.findLadders(beginWord, endWord, wordList)
