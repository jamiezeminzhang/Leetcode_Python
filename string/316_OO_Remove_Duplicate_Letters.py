# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 17:58:13 2016

316. Remove Duplicate Letters

Total Accepted: 8941 Total Submissions: 37504 Difficulty: Medium

Given a string which contains only lowercase letters, remove duplicate letters so that every 
letter appear once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

Example:
Given "bcabc"
Return "abc"

Given "cbacdcbc"
Return "acdb"


关于题意字典序的理解：
不是说把输出结果排序一下就好了。这样是不对的。
理解的是，你的输出需要从原序列中得到，也就是说，原序列删掉一些字，不改变相对位置，可以得到你的输出。
然后要求输出的字典序最小。

*** Another Solution  1 ***
*** DFS

def removeDuplicateLetters(self, s):
    # The order comes from here ! sorted !!!!
    for c in sorted(set(s)):
        suffix = s[s.index(c):]
        if set(suffix) == set(s):
            return c + self.removeDuplicateLetters(suffix.replace(c, ''))
    return ''

*** Another Solution 2 ***
def removeDuplicateLetters(self, s):
    result = ''
    while s:
        i = min(map(s.rindex, set(s)))
        c = min(s[:i+1])
        result += c
        s = s[s.index(c):].replace(c, '')
    return result


@author: Jamie
"""

class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        # record the last position of each letter
        rindex = {c:i for i, c in enumerate(s)}
        result = ''
        
        for i,c in enumerate(s):
            if c not in result:
                # if c < last letter in the result 
                # and there is still at least one  this letter after c
                # we can currently remove this letter and add c
                while c < result[-1:] and i < rindex[result[-1]]:
                    result = result[:-1]
                result += c
        return result