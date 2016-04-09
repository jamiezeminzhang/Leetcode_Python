# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 01:03:59 2016

128. Longest Consecutive Sequence My Submissions Question
Total Accepted: 58261 Total Submissions: 186354 Difficulty: Hard
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.

解题思路：使用一个哈希表，在Python中是字典dict数据类型。dict中的映射关系是{x in num：False}，
这个表示num中的x元素没有被访问过，如果被访问过，则为True。如果x没有被访问过，
检查x+1，x+2...，x-1，x-2是否在dict中，如果在dict中，就可以计数。最后可以求得最大长度。

@author: zeminzhang
"""

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {x: False for x in nums}
        maxLen = -1
        for i in dic:
            if dic[i] == False:
                cur_right, len_right = i+1, 0
                while cur_right in dic and dic[cur_right] == False:
                    dic[cur_right] = True
                    cur_right +=1; len_right += 1
                
                cur_left, len_left = i-1, 0
                while cur_left in dic and dic[cur_left] == False:
                    dic[cur_left] = True
                    cur_left -=1; len_left += 1
                maxLen = max(maxLen, 1+len_left+len_right)
        return maxLen
        
sol = Solution()
print sol.longestConsecutive([0,-1])