# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 10:08:07 2016

212. Word Search II  

Total Accepted: 18268 Total Submissions: 95077 Difficulty: Hard

Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

For example,
Given words = ["oath","pea","eat","rain"] and board =

[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
Return ["eat","oath"].
Note:
You may assume that all inputs are consist of lowercase letters a-z.

click to show hint.

You would need to optimize your backtracking to pass the larger test. Could you stop backtracking earlier?

If the current candidate does not exist in all words' prefix, you could stop backtracking immediately. What kind of data structure could answer such query efficiently? Does a hash table work? Why or why not? How about a Trie? If you would like to learn how to implement a basic trie, please work on this problem: Implement Trie (Prefix Tree) first.

@author: Jamie
"""

class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.isWord = False

class Trie(object):
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for w in word:
            if w not in node.children:
                node.children[w] = TrieNode()
            node = node.children[w]
        node.isWord = True
    
    def search(self, word):
        node = self.root
        for w in word:
            if w not in node.children:
                return False
            node = node.children[w]
        return node.isWord

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        m, n = len(board), len(board[0])
        
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        dz = zip([1,0,-1,0],[0,1,0,-1])
        visited = [[False]*n for _ in range(m)]
        
        def dfs(s, node, x, y):
            node = node.children.get(board[x][y])
            if not node: return
            visited[x][y] = True
            
            for z in dz:
                nx, ny = x+z[0], y+z[1]
                if nx>=0 and nx<m and ny>=0 and ny<n and not visited[nx][ny]:
                    dfs(s+board[nx][ny], node, nx, ny)
            
            if node.isWord:
                res.add(s)
            visited[x][y] = False
        
        res = set()
        for x in range(m):
            for y in range(n):
                dfs(board[x][y], trie.root, x, y)
        
        return sorted(list(res))
                    
        