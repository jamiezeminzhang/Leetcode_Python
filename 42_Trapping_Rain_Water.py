# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 23:53:00 2016

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

For example, 
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.

A better solution:

解题思路：模拟法。开辟一个数组leftmosthigh，leftmosthigh[i]为A[i]之前的最高的bar值，
然后从后面开始遍历，用rightmax来记录从后向前遍历遇到的最大bar值，
那么min(leftmosthigh[i], rightmax)-A[i]就是在第i个bar可以储存的水量。
例如当i=9时，此时leftmosthigh[9]=3,而rightmax=2，则储水量为2-1=1，依次类推即可。
这种方法还是很巧妙的。时间复杂度为O(N)。

class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        leftmosthigh = [0 for i in range(len(A))]
        leftmax = 0
        for i in range(len(A)):
            if A[i] > leftmax: leftmax = A[i]
            leftmosthigh[i] = leftmax
        sum = 0
        rightmax = 0
        for i in reversed(range(len(A))):
            if A[i] > rightmax: rightmax = A[i]
            if min(rightmax, leftmosthigh[i]) > A[i]:
                sum += min(rightmax, leftmosthigh[i]) - A[i]
        return sum

@author: zeminzhang
"""
# my own solution
class Solution(object):
    
    def buildfull(self, height):
        # find the first non zero start
        start = 0
        length = len(height)
        for i in range(length):
            if height[i]>0:
                start = i
                break
        if start == length-1:
            return 0
        
        # build the full shape
        while start < length-1:
            for i in range(start+1,length):
                if height[i] >= height[start]:
                    height[start:i] = [height[start] for x in range(start,i)]
                    start = i
                    break
                if i == length-1:
                    start += 1
        return height
        
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height)==0 or len(height) == 1 or len(height) ==2:
            return 0
               
        sum1 = sum(height)
        height2 = self.buildfull(height)
        # you need to run the reverse list again for the case like [4,2,3]
        height2.reverse()
        height3 = self.buildfull(height2)
        
        sum3 = sum(height3)
        return sum3-sum1
        
sol = Solution()
print sol.trap([0,1,0,2,1,0,1,3,2,1,2,1])
print sol.trap([2,0,2])
print sol.trap([4,2,3])