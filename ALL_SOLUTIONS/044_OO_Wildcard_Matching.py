# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 10:46:45 2016

Implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "*") → true
isMatch("aa", "a*") → true
isMatch("ab", "?*") → true
isMatch("aab", "c*a*b") → false

解题思路：又是一个极其巧妙的解法。

Analysis:

For each element in s
If *s==*p or *p == ? which means this is a match, then goes to next element s++ p++.
If p=='*', this is also a match, but one or many chars may be available, so let us 
save this *'s position and the matched s position.
If not match, then we check if there is a * previously showed up,
       if there is no *,  return false;
       if there is an *,  we set current p to the next element of *, and set 
       current s to the next saved s position.

e.g.

abed
?b*d**

a=?, go on, b=b, go on,
e=*, save * position star=3, save s position ss = 3, p++
e!=d,  check if there was a *, yes, ss++, s=ss; p=star+1
d=d, go on, meet the end.
check the rest element in p, if all are *, true, else false;

Note that in char array, the last is NOT NULL, to check the end, use  "*p"  or "*p=='\0'".

@author: zeminzhang
"""

class Solution:
    # @param s, an input string
    # @param p, a pattern string
    # @return a boolean
    # @good solution! use 'aaaabaaaab' vs 'a*b*b' as an example
    def isMatch(self, s, p):
        pPointer=sPointer=ss=0; star=-1
        while sPointer<len(s):
            if pPointer<len(p) and (s[sPointer]==p[pPointer] or p[pPointer]=='?'):
                sPointer+=1; pPointer+=1
                continue
            if pPointer<len(p) and p[pPointer]=='*':
                star=pPointer; pPointer+=1; ss=sPointer;
                continue
            if star!=-1:
                pPointer=star+1; ss+=1; sPointer=ss
                continue
            return False
        while pPointer<len(p) and p[pPointer]=='*':
            pPointer+=1
        if pPointer==len(p): return True
        return False