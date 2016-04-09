# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 08:48:07 2016

229. Majority Element II My Submissions Question

Total Accepted: 22699 Total Submissions: 90238 Difficulty: Medium
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times. 
The algorithm should run in linear time and in O(1) space.

解题思路：
可以从Moore投票算法中得到一些启发

参考LeetCode Discuss（https://leetcode.com/discuss/43248/boyer-moore-majority-vote-algorithm-and-my-elaboration）

观察可知，数组中至多可能会有2个出现次数超过 ⌊ n/3 ⌋ 的众数

记变量n1, n2为候选众数； c1, c2为它们对应的出现次数

遍历数组，记当前数字为num

若num与n1或n2相同，则将其对应的出现次数加1

否则，若c1或c2为0，则将其置为1，对应的候选众数置为num

否则，将c1与c2分别减1

最后，再统计一次候选众数在数组中出现的次数，若满足要求，则返回之。

@author: Jamie
"""

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums: return []
        if len(nums) <= 1: return nums
        
        n1, n2 = 0,0
        c1, c2 = 0,0
        for num in nums:
            if num == n1: c1 += 1
            elif num == n2: c2 += 1
            elif c1==0: n1, c1 = num, 1
            elif c2==0: n2, c2 = num, 1
            else:
                c1-=1
                c2-=1
           
        c1, c2 = 0, 0
        for num in nums:
            if num == n1: c1+=1
            if num == n2: c2+=1
        res = []
        if c1> len(nums)/3: res += n1,
        if c2> len(nums)/3 and n2!=n1: res += n2,
        return res

sol = Solution()
print sol.majorityElement([1,2])