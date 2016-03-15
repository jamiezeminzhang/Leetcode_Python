# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 22:51:28 2016

93. Restore IP Addresses My Submissions Question
Total Accepted: 49731 Total Submissions: 220083 Difficulty: Medium
Given a string containing only digits, restore it by returning all possible 
valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)

解题思路：这个明显是用dfs来解决。来一段精致简练的代码吧。

@author: zeminzhang
"""

class Solution:
    # @param s, a string
    # @return a list of strings
    def restoreIpAddresses(self, s):
        def dfs(s, sub, ips, ip):
            if sub == 4:                                        # should be 4 parts
                if s == '':
                    ips.append(ip[1:])                          # remove first '.'
                return
            for i in range(1, 4):                               # the three ifs' order cannot be changed!
                if i <= len(s):                                 # if i > len(s), s[:i] will make false!!!!
                    if int(s[:i]) <= 255:
                        dfs(s[i:], sub+1, ips, ip+'.'+s[:i])
                    if s[0] == '0': break                       # make sure that res just can be '0.0.0.0' and remove like '00'
        ips = []
        dfs(s, 0, ips, '')
        return ips

sol = Solution()
print sol.restoreIpAddresses('0000')