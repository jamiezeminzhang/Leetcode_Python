# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 23:23:41 2016

87. Scramble String My Submissions Question
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

My solution!!!!

1. find the partition point first (both in order and reverse)
2. note that there may be multiple such points, save them all
3. dfs the partition, check the substrings divided by the partition point

@author: zeminzhang
"""

class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        length1 = len(s1)
        length2 = len(s2)
        if length1 != length2: return False        
        if s1 == s2: return True
        if length1 == 1 and length2 == 1:
            if s1 != s2: return False
        if length1 == 2 and length2 == 2:
            if (s1[0] == s2[1] and s1[1] == s2[0]) or (s1 == s2):
                return True
            else:
                return False
        # first find the partition point (one way and reversed one)
        dic1, dic2, dic3 = {}, {}, {}
        idx1, idx2 = 0, length1-1
        idx1_list, idx2_list = [], []
        flag, reverse_flag = 0, 0
        while idx1<length1:
            if s1[idx1] in dic1:
                dic1[s1[idx1]] += 1
            else:
                dic1[s1[idx1]] = 1
            
            if s2[idx1] in dic2:
                dic2[s2[idx1]] += 1
            else:
                dic2[s2[idx1]] = 1
            
            if s2[idx2] in dic3:
                dic3[s2[idx2]] += 1
            else:
                dic3[s2[idx2]] = 1
            
            if idx1 != length1-1:
                if dic1 == dic2: 
                    flag = 1
                    idx1_list.append(idx1)
                if dic1 == dic3: 
                    reverse_flag = 1
                    idx2_list.append(idx2)
            idx1 += 1
            idx2 -= 1
        
        if flag == 0 and reverse_flag == 0:
            return False
        elif flag == 1 and reverse_flag==0:
            res = False
            for i in idx1_list:
                res = ( res or (self.isScramble(s1[:i+1],s2[:i+1]) and self.isScramble(s1[i+1:],s2[i+1:])) )
            return res
        elif reverse_flag == 1 and flag == 0:
            res = False
            for i in idx2_list:
                j = length1-1-i
                res = (res or (self.isScramble(s1[:j+1],s2[i:]) and self.isScramble(s1[j+1:],s2[:i])))
            return res
        elif flag == 1 and reverse_flag == 1:
            res1 = False
            for i in idx1_list:
                res1 = ( res1 or (self.isScramble(s1[:i+1],s2[:i+1]) and self.isScramble(s1[i+1:],s2[i+1:])) )
            res2 = False
            for i in idx2_list:
                j = length1-1-i
                res2 = (res2 or (self.isScramble(s1[:j+1],s2[i:]) and self.isScramble(s1[j+1:],s2[:i])))
            return (res1 or res2)
            
sol = Solution()
print sol.isScramble('a','b')
print sol.isScramble('abb','bba')
print sol.isScramble('rgeat','great')
print sol.isScramble('abcd','bdac')
print sol.isScramble("hobobyrqd","hbyorqdbo")
print sol.isScramble("cbcccccbbabcbac","bbccaccbcbcabcc")