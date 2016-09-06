# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 14:37:40 2016

214. Shortest Palindrome My Submissions Question

Total Accepted: 16240 Total Submissions: 85929 Difficulty: Hard

Given a string S, you are allowed to convert it to a palindrome by adding characters in front of it. 
Find and return the shortest palindrome you can find by performing this transformation.

For example:

Given "aacecaaa", return "aaacecaaa".

Given "abcd", return "dcbabcd".

记原始字符串为s，s的反转字符串为rev_s。

构造字符串l = s + '#' + rev_s，其中'#'为s中不会出现的字符，添加'#'是为了处理输入为空字符串的情形。

对字符串l执行KMP算法，可以得到“部分匹配数组”p（也称“失败函数”）

我们只关心p数组的最后一个值p[-1]，因为它表明了rev_s与s相互匹配的最大前缀长度。

最后只需要将rev_s的前k个字符与原始串s拼接即可，其中k是s的长度len(s)与p[-1]之差。

http://blog.csdn.net/v_july_v/article/details/7041827
        
@author: Jamie
"""

class Solution(object):
    # @param {string} s
    # @return {string}
    def shortestPalindrome(self, s):
        rev_s = s[::-1]
        l = s + '#' + rev_s
        p = [0] * len(l)
        for i in range(1, len(l)):
            j = p[i - 1]
            while j > 0 and l[i] != l[j]:
                j = p[j - 1]
            p[i] = j + (l[i] == l[j])
        return rev_s[: len(s) - p[-1]] + s

sol = Solution()
print sol.shortestPalindrome('cbbcab')