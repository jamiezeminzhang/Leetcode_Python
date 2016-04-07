# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 08:08:50 2016

136. Single Number

Total Accepted: 112256 Total Submissions: 231990 Difficulty: Medium

Given an array of integers, every element appears twice except for one. 
Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement 
it without using extra memory?

XOR: 不同是1， 相同是0

解题思路：这题考的是位操作。只需要使用异或(xor)操作就可以解决问题。异或操作的定义为：
x ^ 0 = x; x ^ x = 0。用在这道题里面就是：y ^ x ^ x = y; x ^ x = 0; 
举个例子：序列为：1122334556677。4是那个唯一的数，之前的数异或操作都清零了，
之后的数：4 ^ 5 ^ 5 ^ 6 ^ 6 ^ 7 ^ 7 = 4 ^ ( 5 ^ 5 ^ 6 ^ 6 ^ 7 ^ 7 ) = 4 ^ 0 = 4。问题解决。

*** 1 line solution ***
*** remember these useful functions***
*** filter, map, reduce ****

class Solution(object):
    def singleNumber(self, nums):
        return reduce(lambda x,y:x^y, nums )
        
@author: zeminzhang
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = nums[0]
        for i in range(1,len(nums)):
            ans = ans^nums[i]
        return ans
