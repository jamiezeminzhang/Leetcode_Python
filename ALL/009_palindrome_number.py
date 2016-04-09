# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 15:29:25 2015

LeetCode #9 Palindrome Number

Determine whether an integer is a palindrome. Do this without extra space.

click to show spoilers.
Some hints:

Could negative integers be palindromes? (ie, -1)

If you are thinking of converting the integer to string, note the restriction of using extra space.

You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?

There is a more generic way of solving this problem.


@author: zzhang
"""

class Solution:
    # @param {integer} x
    # @return {boolean}
    def isPalindrome(self, x):
        if x<0:
            return False
        elif x==0:
            return True
        else:
            # decide the length of x
            l = 1
            while x/10**l >0:
                l +=1
            
            flag = 1
            if l%2 == 0:
                mid = l/2-1
            else:
                mid = (l-1)/2
            
            for i in range(mid+1):
                j = l-1-i
                
                a = x/10**(l-1-i) - x/10**(l-i)*10
                b = x/10**(l-1-j) - x/10**(l-j)*10
                if a!=b:
                    flag = 0
                    break
            
            if flag == 1:
                return True
            else:
                return False