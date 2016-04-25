# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 14:43:28 2016

273. Integer to English Words

Total Accepted: 12463 Total Submissions: 69075 Difficulty: Medium

Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.

For example,
123 -> "One Hundred Twenty Three"
12345 -> "Twelve Thousand Three Hundred Forty Five"
1234567 -> "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
Hint:

Did you see a pattern in dividing the number into chunk of words? For example, 123 and 123000.
Group the number by thousands (3 digits). You can write a helper function that takes a number less than 1000 and convert just that chunk to words.
There are many edge cases. What are some good test cases? Does your code work with input such as 0? Or 1000010? (middle chunk is zero and should not be printed out)

@author: Jamie
"""

class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        dic1 = {'0':'Zero','1':'One','2':'Two','3':'Three','4':'Four','5':'Five','6':'Six','7':'Seven','8':'Eight','9':'Nine','10':'Ten','11':'Eleven','12':'Twelve','13':'Thirteen','14':'Fourteen','15':'Fifteen','16':'Sixteen','17':'Seventeen','18':'Eighteen','19':'Nineteen'}
        dic3 = {'2':'Twenty','3':'Thirty','4':'Forty','5':'Fifty','6':'Sixty','7':'Seventy','8':'Eighty','9':'Ninety'}
        lis = ['Hundred','Thousand','Million','Billion']
        
        def num3(s):
            while s[0] =='0' and len(s)>=2: s = s[1:]
            if len(s) == 1: return dic1[s]
            if len(s) == 2:
                if int(s) <=19: return dic1[s]
                else:
                    if s[1] != '0': return dic3[s[0]]+' '+dic1[s[1]]
                    else: return dic3[s[0]]
            if len(s) == 3:
                if int(s[1:]) != 0: return dic1[s[0]]+' '+lis[0]+' '+num3(s[1:])
                else: return dic1[s[0]]+' '+lis[0]
                    
        s = str(num)
        while s[0] =='0' and len(s)>=2: s = s[1:]
        
        length = len(s)
        if length <=3: return num3(s)
        elif length <=6 :
            if int(s[-3:]) != 0:
                return num3(s[:-3]) + ' ' + lis[1] + ' ' + num3(s[-3:])
            else:
                return num3(s[:-3]) + ' ' + lis[1]
        elif length <=9 :
            tmp1 = ' '+num3(s[-6:-3]) + ' ' + lis[1] if int(s[-6:-3])!=0 else ''
            tmp2 = ' '+num3(s[-3:]) if int(s[-3:]) != 0 else ''
            return num3(s[:-6]) + ' ' + lis[2] + tmp1 + tmp2
        else: 
            tmp1 = ' '+num3(s[-9:-6]) + ' ' + lis[2] if int(s[-9:-6])!=0 else ''
            tmp2 = ' '+num3(s[-6:-3]) + ' ' + lis[1] if int(s[-6:-3])!=0 else ''
            tmp3 = ' '+num3(s[-3:]) if int(s[-3:]) != 0 else ''
            return num3(s[:-9]) + ' ' + lis[3] + tmp1 + tmp2 + tmp3