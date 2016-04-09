# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 08:13:53 2016

211. Add and Search Word - Data structure design My Submissions Question

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

最好不要.val
用.isWord
参考 212题目
@author: Jamie
"""

class TrieNode(object):
    def __init__(self):
        self.val = None
        self.children = {}
        
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
        word += '#'
        root = self.root
        while word and word[0] in root.children:
            root = root.children[word[0]]
            word = word[1:]
        
        while word:
            node = TrieNode()
            node.val = word[0]
            root.children[word[0]] = node
            root = node
            word = word[1:]
        
    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        if word == '': return False
        word += '#'
        
        def dfs(root, word):
            if not word: return True
            else:
                if word[0] != '.':
                    if word[0] in root.children:
                        return dfs(root.children[word[0]], word[1:])
                    else:
                        return False
                else:
                    for i in root.children:
                        if dfs(root.children[i], word[1:]):
                            return True
                    return False

        return dfs(self.root, word)
        

# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")