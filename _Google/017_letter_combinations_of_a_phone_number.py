# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 12:25:52 2015

LeetCode #17 Letter Combinations of a Phone Number

Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.

class Solution(object):
    def letterCombinations(self, digits):
        dic = {'2':['a','b','c'],\
               '3':['d','e','f'],\
               '4':['g','h','i'],\
               '5':['j','k','l'],\
               '6':['m','n','o'],\
               '7':['p','q','r','s'],\
               '8':['t','u','v'],\
               '9':['w','x','y','z']}
        num_list = list(digits)[::-1]
        ans = []
        while num_list:
            cur_digit = num_list.pop()
            if not ans:
                for letter in dic[cur_digit]:
                    ans.append(letter)
            else:
                new = list(ans)
                cur_ans = []
                for letter in dic[cur_digit]:
                    tmp = list(new)
                    for i in range(len(tmp)):
                        tmp[i] += letter
                    cur_ans += tmp
                ans = cur_ans
        return ans
        


@author: zzhang
"""

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dic = {'2':['a','b','c'], '3':['d','e','f'], '4':['g','h','i'], '5':['j','k','l'], \
        '6':['m','n','o'], '7':['p','q','r','s'], '8':['t','u','v'], '9':['w','x','y','z']}
        
        def dfs(s, lis):
            if s == '': return lis
            elif lis == []: 
                return dfs(s[1:], dic[s[0]])
            else:
                lis = [i+letter for i in lis for letter in dic[s[0]]]
                return dfs(s[1:], lis)
                
        return dfs(digits,[])




sol = Solution();
print sol.letterCombinations(23)