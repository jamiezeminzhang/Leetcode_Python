# -*- coding: utf-8 -*-
"""
Created on Thursday Aug 4 10:18:41 2016

288. Unique Word Abbreviation

Total Accepted: 12442
Total Submissions: 78615
Difficulty: Easy

An abbreviation of a word follows the form <first letter><number><last letter>. Below are some examples of word abbreviations:

a) it                      --> it    (no abbreviation)

     1
b) d|o|g                   --> d1g

              1    1  1
     1---5----0----5--8
c) i|nternationalizatio|n  --> i18n

              1
     1---5----0
d) l|ocalizatio|n          --> l10n
Assume you have a dictionary and given a word, find whether its abbreviation is unique in the dictionary. A word's abbreviation is unique if no other word from the dictionary has the same abbreviation.

Example: 
Given dictionary = [ "deer", "door", "cake", "card" ]

isUnique("dear") -> false
isUnique("cart") -> true
isUnique("cane") -> false
isUnique("make") -> true
@author: zzhang


"""

class ValidWordAbbr(object):
    def __init__(self, dictionary):
        """
        initialize your data structure here.
        :type dictionary: List[str]
        """
        self.d = collections.defaultdict(int)
        self.d2 = set(dictionary)
        for word in self.d2:
            word_ab = self.getAbbrev(word)
            self.d[word_ab] += 1
    
    def getAbbrev(self, word):
        if len(word)<=2:
            return word
        else:
            return word[0] + str(len(word)-2) + word[-1]

    def isUnique(self, word):
        """
        check if a word is unique.
        :type word: str
        :rtype: bool
        """
        word_ab = self.getAbbrev(word)
        if word in self.d2:
            return self.d[word_ab] <= 1
        else:
            return word_ab not in self.d


# Your ValidWordAbbr object will be instantiated and called as such:
# vwa = ValidWordAbbr(dictionary)
# vwa.isUnique("word")
# vwa.isUnique("anotherWord")
