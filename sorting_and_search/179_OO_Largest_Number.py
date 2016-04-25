# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 05:21:38 2016

179. Largest Number

Total Accepted: 43331 Total Submissions: 229885 Difficulty: Medium

Given a list of non negative integers, arrange them such that they form the largest number.

For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.

** My hint
333 > 33300
9 > 84

[55543, 555 ,44] -> 55544 55543
[55543, 555, 42] -> 55543 55542

SOLUTION 1:

参考http://bookshadow.com/weblog/2015/01/13/leetcode-largest-number/的解法：

贪心思路：对于两个备选数字a和b，如果str(a) + str(b) > str(b) + str(a)，则a在b之前，否则b在a之前

按照此原则对原数组从大到小排序即可

@author: Jamie
"""

class Solution(object):
    def compare2(self, num1, num2):
        n1 = int( str(num1) + str(num2) )
        n2 = int( str(num2) + str(num1) )
        return True if n1>n2 else False
        
    def quicksort2(self, nums):
        if len(nums) <= 1: return nums
        pv = nums[0]
        return self.quicksort2([x for x in nums[1:] if self.compare2(x,pv)]) + \
            [pv] + \
            self.quicksort2([x for x in nums[1:] if not self.compare2(x,pv) ])
        
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = self.quicksort2(nums)
        s = ''
        for i in nums:
            s += str(i)
        return s if s[0] != '0' else '0'
        
sol = Solution()
#print sol.quicksort2([2,1])
#print sol.largestNumber([55543,555,43])
#print sol.compare2(1,1)
#print sol.quicksort2([1,1,1])
print sol.largestNumber([1])