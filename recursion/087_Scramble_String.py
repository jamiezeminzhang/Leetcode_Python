# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 23:23:41 2016

87. Scramble String

Total Accepted: 41783 Total Submissions: 161251 Difficulty: Hard

Given a string s1, we may represent it as a binary tree by partitioning it to 
two non-empty substrings recursively.

Below is one possible representation of s1 = "great":

    great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t
To scramble the string, we may choose any non-leaf node and swap its two children.

For example, if we choose the node "gr" and swap its two children, it produces 
a scrambled string "rgeat".

    rgeat
   /    \
  rg    eat
 / \    /  \
r   g  e   at
           / \
          a   t
We say that "rgeat" is a scrambled string of "great".

Similarly, if we continue to swap the children of nodes "eat" and "at", it 
produces a scrambled string "rgtae".

    rgtae
   /    \
  rg    tae
 / \    /  \
r   g  ta  e
       / \
      t   a
We say that "rgtae" is a scrambled string of "great".

Given two strings s1 and s2 of the same length, determine if s2 is a scrambled 
string of s1.

@author: zeminzhang
"""

class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1)!=len(s2) or sorted(s1)!=sorted(s2):
            return False
        if len(s1)<4 or s1==s2: return True
        f = self.isScramble
        for i in range(1,len(s1)):
            if f(s1[:i],s2[:i]) and f(s1[i:],s2[i:]) or \
            f(s1[:i],s2[-i:]) and f(s1[i:],s2[:-i]):
                return True
        return False