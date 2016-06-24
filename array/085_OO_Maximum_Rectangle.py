# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 06:34:51 2016

85. Maximal Rectangle

Total Accepted: 37534 Total Submissions: 163466 Difficulty: Hard

Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle 
containing all ones and return its area.

可以用上题的方法做。对每一行，求出从这一行向下的连续的1的个数统计成的histogram。
算出最大的rectangle，也就算出了以这个row为顶边的最大的rectangle的面积。所有行都算一遍就可以。

@author: zeminzhang
"""

class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        
        if matrix == []: return 0
        
        m,n = len(matrix), len(matrix[0])
        maxArea = 0
        for i in range(m):
            a = [0 for x in range(n)]
            for j in range(n): # compute a[j]
                for tmp in range(i,m):
                    if matrix[tmp][j] == '1':
                        a[j] += 1
                    else:
                        break
            maxArea = max(maxArea, self.maxRectangle(a))
        return maxArea
                
    
    def maxRectangle(self,nums):
        length = len(nums)
        if length == 0: return 0
        if length == 1: return nums[0]
        
        nums = nums+[0]
        stack = []
        i, maxArea = 0,0
        while i <= length:
            if not stack or nums[stack[-1]] <= nums[i]:
                stack.append(i)
                i += 1
            else:
                t = stack.pop()
                maxArea = max(maxArea, nums[t]*(i if not stack else i-stack[-1]-1 ))
        return maxArea
        
sol = Solution()
#print sol.maxRectangle([2,1,5,6,2,3])
print sol.maximalRectangle(['0100','0100','0100','0100'])