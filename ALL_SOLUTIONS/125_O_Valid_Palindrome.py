# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 07:35:31 2016

125. Valid Palindrome My Submissions Question

Total Accepted: 87062 Total Submissions: 375746 Difficulty: Easy
Given a string, determine if it is a palindrome, considering only alphanumeric 
characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to 
ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.

************************************
Key: Remember function str.isalnum()
************************************

###My solution: TLE #### Given below
class Solution(object):
    def isPalindrome(self, s):
        length = len(s)
        if length <= 1: return True
        
        string = ""
        for i in range(length):
            if (s[i] >= 'a' and s[i] <= 'z') or (s[i]>='A' and s[i]<= 'Z')\
            or (s[i] >= '0' and s[i] <= '9'):
                string += s[i]
        string = string.lower()
        length2 = len(string)
        mid = length2/2
        for i in range(mid):
            if string[i]!=string[length2-1-i]: return False
        return True

** Correct codes given below 81.21% ***
@author: zeminzhang
"""
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        length = len(s)
        if length <=1: return True
        start, end = 0, length-1
        while start<end:
            while start<end and not s[start].isalnum():
                start += 1
            while start<end and not s[end].isalnum():
                end -= 1
            if start<end and s[start].lower() != s[end].lower():
                return False
            start += 1
            end -= 1
        return True

        