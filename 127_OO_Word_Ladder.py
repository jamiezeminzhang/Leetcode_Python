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

###### My Solution : TLE #######

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        res = []
        wordList = list(wordList)
        Solution.min = 100000000
        def dfs(beginWord, endWord, wordList, resList):
            for word in wordList:
                if self.dis2(beginWord, word):
                    resList.append(word)
                    if word == endWord: 
                        if len(resList) < Solution.min:
                            Solution.min = len(resList)
                        res.append(resList)
                        return
                    tmp = list(wordList)
                    tmp.remove(word)
                    dfs(word,endWord,tmp,resList)

        dfs(beginWord, endWord, wordList + [endWord], [])
        return Solution.min-1
        
    def dis2(self, word1, word2):
        length = len(word1)
        if length == 0 : return True
        if length == 1: return True if word1[0] == word2[0] else False
        for i in range(length):
            for x in 'qwertyuiopasdfghjklzxcvbnm':
                if word1[:i] + x + word1[i+1:] == word2: return True
        return False

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