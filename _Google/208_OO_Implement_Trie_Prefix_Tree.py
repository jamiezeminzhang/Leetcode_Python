# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 22:18:16 2016

208. Implement Trie (Prefix Tree)

Total Accepted: 28963 Total Submissions: 114940 Difficulty: Medium

Implement a trie with insert, search, and startsWith methods.

Note:
You may assume that all inputs are consist of lowercase letters a-z.

@author: Jamie
"""

class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = {}
        self.isWord = False

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        for letter in word:
            if letter not in node.children:
                node.children[letter] = TrieNode()
            node = node.children[letter]
        node.isWord = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for letter in word:
            if letter not in node.children:
                return False
            node = node.children[letter]
        return node.isWord
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for letter in prefix:
            if letter not in node.children:
                return False
            node = node.children[letter]
        return True

# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")