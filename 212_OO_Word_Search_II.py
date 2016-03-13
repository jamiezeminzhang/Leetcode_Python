# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 10:08:07 2016

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
        for letter in word:
            child = node.children.get(letter)
            if not child:
                child = TrieNode()
                node.children[letter] = child
            node = child
        node.isWord = True
        
    def delete(self, word):
        node = self.root
        queue = []
        
        for letter in word:
            queue.append((letter, node))
            child = node.children.get(letter)
            if not child: return False
            node = child
            
        # check: last letter of the word, the isWord label should be True
        if not node.isWord: return False
        
        # case1: if this node has children, like we are deleting ab, but there's a word abc
        # then we just change the node b's isWord label to False and we are done
        if len(node.children): node.isWord = False
        
        # Otherwise, delete the node
        else:
            for letter, node in reversed(queue):     # Reversed QUEUE!!!!!
                del node.children[letter]
                if len(node.children) or node.isWord: #isWord=True means the last node
                    break
        return True

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        h, w = len(board), len(board[0])
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        dz = zip([1,0,-1,0],[0,1,0,-1])
        visited = [[False]*w for x in range(h)]
        res = []
        
        def dfs(word, node, x, y):
            node = node.children.get(board[x][y])
            if not node: return
            visited[x][y] = True
            
            for z in dz:
                nx = x+z[0]; ny=y+z[1]
                if nx>=0 and nx<h and ny>=0 and ny<w and not visited[nx][ny]:
                    dfs(word+board[nx][ny], node, nx, ny)
            if node.isWord:
                res.append(word)
                trie.delete(word)
            visited[x][y] = False
        
        for x in range(h):
            for y in range(w):
                dfs(board[x][y], trie.root, x, y)
        
        return sorted(res)
            
            
            
        