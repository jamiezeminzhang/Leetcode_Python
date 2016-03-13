# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 21:46:04 2016

299. Bulls and Cows My Submissions Question

Total Accepted: 19505 Total Submissions: 68234 Difficulty: Easy
You are playing the following Bulls and Cows game with your friend: You write down a number and 
ask your friend to guess what the number is. Each time your friend makes a guess, you provide a hint 
that indicates how many digits in said guess match your secret number exactly in both digit and 
position (called "bulls") and how many digits match the secret number but locate in the wrong 
position (called "cows"). Your friend will use successive guesses and hints to eventually derive 
the secret number.

For example:

Secret number:  "1807"
Friend's guess: "7810"
Hint: 1 bull and 3 cows. (The bull is 8, the cows are 0, 1 and 7.)
Write a function to return a hint according to the secret number and friend's guess, use A to 
indicate the bulls and B to indicate the cows. In the above example, your function should return "1A3B".

Please note that both secret number and friend's guess may contain duplicate digits, for example:

Secret number:  "1123"
Friend's guess: "0111"
In this case, the 1st 1 in friend's guess is a bull, the 2nd or 3rd 1 is a cow, and your function 
should return "1A1B".
You may assume that the secret number and your friend's guess only contain digits, and their 
lengths are always equal.

@author: Jamie
"""

class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        length = len(secret)
        count_a, count_b = 0, 0
        i= 0
        while i<length:
            if secret[i] == guess[i]:
                count_a += 1
            i+=1
        
        dic1 = collections.defaultdict(int)
        dic2 = collections.defaultdict(int)
        for i in secret:
            dic1[i] += 1
        for i in guess:
            dic2[i] += 1
        for i in dic1:
            count_b += min(dic1[i], dic2[i])
        
        return str(count_a) + 'A' + str(count_b-count_a) + 'B'