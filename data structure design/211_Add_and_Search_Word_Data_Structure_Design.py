# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 08:13:53 2016

211. Add and Search Word - Data structure design 

Total Accepted: 19775 Total Submissions: 97605 Difficulty: Medium

Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z 
or .. A . means it can represent any one letter.

For example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
Note:
You may assume that all words are consist of lowercase letters a-z.


用.isWord
参考 212题目
@author: Jamie
"""

class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.isWord = False

class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        node = self.root
        for w in word:
            if w not in node.children:
                node.children[w] = TrieNode()
            node = node.children[w]
        node.isWord = True
        
        
    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        def search_from_node(node, word):
            if word == '': return node.isWord
            if word[0]!='.':
                if word[0] not in node.children:
                    return False
                return search_from_node(node.children[word[0]],word[1:])
            else:
                for child in node.children:
                    if search_from_node(node.children[child],word[1:]):
                        return True
            return False
            
        return search_from_node(self.root, word)
        
        
        

# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")
        
