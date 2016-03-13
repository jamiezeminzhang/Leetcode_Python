# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 09:35:47 2016

139. Word Break My Submissions Question
Total Accepted: 77066 Total Submissions: 315805 Difficulty: Medium
Given a string s and a dictionary of words dict, determine if s can be segmented 
into a space-separated sequence of one or more dictionary words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".

### My dfs solution: TLE
class Solution(object):
    def wordBreak(self, s, wordDict):
        def dfs(s):
            if len(s) == 0:                 
                Solution.res = True
            else:
                flag = 0
                for i in range(len(s)+1):
                    if s[:i] in wordDict:
                        flag = 1
                        dfs(s[i:])
                if flag == 0:
                    return
        dfs(s)
        return Solution.res
*** 如果只需要一个true false / 活着需要你return一共又多少组解，只要数字的话
用dfs 一般会超时
所以一般用dp
@author: zeminzhang
"""
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        
        length = len(s)
        dp = [False for x in range(length+1)] 
        dp[0] = True
        for i in range(1,length+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
        
        return dp[length]
            

        
sol = Solution()
dic = {"go","goal","goals","special"}
s = "goalspecial"
print sol.wordBreak(s,dic)