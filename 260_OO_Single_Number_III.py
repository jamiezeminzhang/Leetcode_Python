# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 11:31:10 2016

260. Single Number III My Submissions Question

Total Accepted: 25439 Total Submissions: 59645 Difficulty: Medium
Given an array of numbers nums, in which exactly two elements appear only once and all the other 
elements appear exactly twice. Find the two elements that appear only once.

For example:

Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].

Note:
The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?
Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.


首先计算nums数组中所有数字的异或，记为xor

令lowbit = xor & -xor，lowbit的含义为xor从低位向高位，第一个非0位所对应的数字

例如假设xor = 6（二进制：0110），则-xor为（二进制：1010，-6的补码，two's complement）

则lowbit = 2（二进制：0010）

根据异或运算的性质，“同0异1”

记只出现一次的两个数字分别为a与b

可知a & lowbit与b & lowbit的结果一定不同

通过这种方式，即可将a与b拆分开来


Also, please learn how to use reduce:

reduce(function, iterable[, initializer])

and reduce the codes to 3 lines

class Solution(object):
    def singleNumber(self, nums):

        xor = reduce(lambda x,y: x^y, nums)
        n1 = reduce(lambda x,y: x^y if y & xor & -xor else x^0, nums, 0)
        return [n1,n1^xor]
        

@author: Jamie
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor = reduce(lambda x,y: x^y, nums)
        lowbit = xor & -xor
        a, b = 0, 0
        for num in nums:
            if num & lowbit: a^=num
            else: b^= num
        return [a,b]