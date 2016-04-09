# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 19:48:14 2016

338. Counting Bits My Submissions Question
Total Accepted: 1713 Total Submissions: 3091 Difficulty: Medium

Given a non negative integer number num. For every numbers i in the range 
0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example:
For num = 5 you should return [0,1,1,2,1,2].

Follow up:

It is very easy to come up with a solution with run time O(n*sizeof(integer)). 
But can you do it in linear time O(n) /possibly in a single pass?
Space complexity should be O(n).
Can you do it like a boss? Do it without using any builtin function 
like __builtin_popcount in c++ or in any other language.
Hint:

You should make use of what you have produced already.
Divide the numbers in ranges like [2-3], [4-7], [8-15] and so on. And try to 
generate new range from previous.
Or does the odd/even status of the number help you in calculating the number of 1s?


***** My original solution: *****

class Solution(object):
    def countBits(self, num):
        if num==0: return [0]
        res, curr, p = [0,1], [1], int(math.log(num, 2))-1
        for i in range(p): 
            curr += [1+j for j in curr]
            res += curr
        return res + curr[:num-len(res)+1] if num-len(res)+1<len(curr) else \
        res + curr + [1+j for j in curr[:num-len(res)-len(curr)+1]]
@author: zeminzhang
"""

class Solution(object):
    def countBits(self, num):
        if num==0: return[0]
        dp = [0]*(num+1)
        for i in range(1,num+1): dp[i] = dp[i/2] if i%2==0 else dp[i/2]+1
        return dp