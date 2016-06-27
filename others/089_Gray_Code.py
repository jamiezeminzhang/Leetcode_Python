# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 02:58:37 2016

89. Gray Code

Total Accepted: 52667 Total Submissions: 149821 Difficulty: Medium

The gray code is a binary numeral system where two successive values differ 
in only one bit.

Given a non-negative integer n representing the total number of bits in the 
code, print the sequence of gray code. A gray code sequence must begin with 0.

For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:

00 - 0
01 - 1
11 - 3
10 - 2
Note:
For a given n, a gray code sequence is not uniquely defined.

For example, [0,2,3,1] is also a valid gray code sequence according to the 
above definition.

For now, the judge is able to judge based on one instance of gray code sequence. 
Sorry about that.

#### My solution

class Solution(object):
    def grayCodeStr(self,n):
        if n==0: return ['0']
        if n==1: return ['0','1']
        temp = self.grayCodeStr(n-1)
        return ['0'+i for i in temp]+['1'+i for i in temp[::-1]]
        
    def grayCode(self, n):

        res = self.grayCodeStr(n)
        return [int(i,2) for i in res]


格雷码的生成，采用数学的方法。
格雷码还有一种实现方式是根据这个公式来的 G(n) =  B(n) XOR B(n+1), 这也是格雷码和二进制码的转换公式

@author: zeminzhang
"""
class Solution:
    # @return a list of integers
    def grayCode(self, n):
        res=[]
        size=1<<n  # shift n to left ( = 2**n )
        for i in range(size):
            res.append((i>>1)^i)
        return res 