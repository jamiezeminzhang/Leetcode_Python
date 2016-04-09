# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 21:45:27 2016

127. Word Ladder My Submissions Question
Total Accepted: 66019 Total Submissions: 337427 Difficulty: Medium
Given two words (beginWord and endWord), and a dictionary's word list, find 
the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the word list
For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Note:
Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.


Correct one: BFS
http://chaoren.is-programmer.com/posts/43039.html
@author: zeminzhang
"""

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        wordList.add(endWord)
        q = []
        q.append((beginWord,1))
        
        while q:
            curr = q.pop(0)
            currword = curr[0]; currlen = curr[1]
            if currword == endWord: return currlen
            for i in range(len(beginWord)):
                part1, part2 = currword[:i], currword[i+1:]
                for j in 'abcdefghijklmnopqrstuvwxyz':
                    if currword[i] != j:
                        nextword = part1+j+part2
                        if nextword in wordList:
                            q.append((nextword,currlen+1))
                            wordList.remove(nextword)
        return 0
        
sol = Solution()
#beginWord = "hit"
#endWord = "cog"
#wordList = {"hot","dot","dog","lot","log"}
beginWord = "hot"
endWord = "dog"
wordList = {"hot","dot","dog"}
print sol.ladderLength(beginWord, endWord, wordList)
