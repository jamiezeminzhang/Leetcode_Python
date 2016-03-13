# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 04:32:07 2016

84. Largest Rectangle in Histogram My Submissions Question
Total Accepted: 53341 Total Submissions: 226179 Difficulty: Hard

Given n non-negative integers representing the histogram's bar height where 
the width of each bar is 1, find the area of largest rectangle in the histogram.

最直接的算法需要o(n^2)在最坏的情况下。对每一个index，求包含这个index最大的方块的值。
对于全递增序列就是最坏的情况。

网上答案：
要一个栈来存放非递减的height序列, 即碰到大于等于栈顶的就入栈, 碰到小于栈顶的就pop。
对于每个pop出的元素h[stack[top]]，都要计算以它为最低高度的矩形的面积, 高度就是h[stack[top]], 
宽度就是i － stack[-1] - 1, 注意栈中的元素都是非递减的。在h末尾多加一个0的目的是保证栈中的元素都可以被pop出。

detailed algorithm with figures:
http://www.cnblogs.com/lichen782/p/leetcode_Largest_Rectangle_in_Histogram.html

class Solution:
    # @param height, a list of integer
    # @return an integer
    def largestRectangleArea(self, height):
        stack = []
        i = 0
        maxArea = 0
        h = height + [0]
        h_length = len(h)
        while i < h_length:
            # not stack means stack is empty
            if (not stack) or h[stack[-1]] <= h[i]:
                stack.append(i)
                i += 1
            else:
                t = stack.pop()
                maxArea = max(maxArea, h[t] * (i if not stack else i - stack[-1] - 1))
        return maxArea
        
@author: zeminzhang
"""

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        length = len(heights)
        if length == 0: return 0
        if length == 1: return heights[0]
        
        heights = heights + [0]
        stack = []
        i,maxArea = 0, 0
        while i < length+1:
            if not stack or heights[stack[-1]] <= heights[i]:
                stack.append(i)
                i += 1
            else:
                t = stack.pop()
                maxArea = max(maxArea, heights[t]* (i if not stack else i-stack[-1]-1 ) )
        return maxArea
        