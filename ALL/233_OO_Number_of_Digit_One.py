# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 09:52:53 2016

233. Number of Digit One My Submissions Question
Total Accepted: 16061 Total Submissions: 67679 Difficulty: Medium
Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.

For example:
Given n = 13,
Return 6, because digit 1 occurred in the following numbers: 1, 10, 11, 12, 13.


举个例子54215，比如现在求百位上的1（即len是100），54215的百位上是2。看到xx100到xx199的百位上都是1， 
这里xx从0到54，即100->199, 1100->1199...54100->54199, 这些数的百位都是1，百位上的1总数是55*10

如果n是54125,这时由于它的百位是1，先看xx100到xx199，其中xx是0到53，即54*10, 然后看54100到54125，这是26个。
所以百位上的1的总数是54*10 + 26.8 l$ f! |2 {5 }! n" a  t
/ p$ `+ ~1 Q, T6 x6 R
如果n是54025，那么只需要看xx100到xx199中百位上的1，这里xx从0到53，总数为54*10.
5 Q) @" H" @7 |" Q. P  M: o
同理，如果求2的总数，3的总数等等都可以这样分情况解


@author: Jamie
"""

class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=0: return 0
        if n<=9: return 1

        n_string = str(n)
        length = len(n_string)
        res = 0
        for i in range(length):
            if i == 0:
                if n_string[i] == '1': 
                    res += int(n_string[1:]) + 1
                else:
                    res += 10**(length-1)
            elif i == length-1:
                if n_string[i] == '0':
                    res += int(n_string[:-1])
                else:
                    res += int(n_string[:-1]) + 1
            else:
                if n_string[i] == '0':
                    res += int(n_string[:i])*(10**(length-i-1))
                elif n_string[i] == '1':
                    res += int(n_string[:i])*(10**(length-i-1)) + int(n_string[i+1:]) + 1
                else:
                    res += (int(n_string[:i]) + 1) * (10**(length-i-1))
        return res

sol = Solution()
print sol.countDigitOne(1)