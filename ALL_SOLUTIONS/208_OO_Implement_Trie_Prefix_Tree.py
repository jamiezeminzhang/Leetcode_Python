# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 22:18:16 2016

208. Implement Trie (Prefix Tree) My Submissions Question

Total Accepted: 28963 Total Submissions: 114940 Difficulty: Medium

Implement a trie with insert, search, and startsWith methods.

Note:
You may assume that all inputs are consist of lowercase letters a-z.

*** My only beats 6% ***

*** A better solution ***

class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.childs = dict()
        self.isWord = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    # @param {string} word
    # @return {void}
    # Inserts a word into the trie.
    def insert(self, word):
        node = self.root
        for letter in word:
            child = node.childs.get(letter)
            if child is None:
                child = TrieNode()
                node.childs[letter] = child
            node = child
        node.isWord = True

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the trie.
    def search(self, word):
        node = self.root
        for letter in word:
            node = node.childs.get(letter)
            if node is None:
                return False
        return node.isWord

    # @param {string} prefix
    # @return {boolean}
    # Returns if there is any word in the trie
    # that starts with the given prefix.
    def startsWith(self, prefix):
        node = self.root
        for letter in prefix:
            node = node.childs.get(letter)
            if node is None:
                return False
        return True

@author: Jamie
"""

class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.val = None
        self.next = {}

class Trie(object):
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        word += '#'
        root = self.root
        while word and word[0] in root.next:
            root = root.next[word[0]]
            word = word[1:]
        
        if len(word)>0:
            while word:
                node = TrieNode(); node.val = word[0]
                root.next[word[0]] = node
                root = node
                word = word[1:]
        
    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        word += '#'
        root = self.root
        while word:
            if word[0] not in root.next:
                return False
            else:
                root = root.next[word[0]]
                word = word[1:]
        return True
        
    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        root = self.root
        while prefix:
            if prefix[0] not in root.next:
                return False
            else:
                root = root.next[prefix[0]]
                prefix = prefix[1:]
        return True

# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")