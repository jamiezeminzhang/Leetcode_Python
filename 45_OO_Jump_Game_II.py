# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 10:59:58 2016

Given an array of non-negative integers, you are initially positioned at the 
first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

For example:
Given array A = [2,3,1,1,4]

The minimum number of jumps to reach the last index is 2. (Jump 1 step from 
index 0 to 1, then 3 steps to the last index.)

Note:
You can assume that you can always reach the last index.

我的算法超时，用的dp的思路
class Solution(object):
    def jump(self, nums):
        MAX_val = 2**31-1
        length = len(nums)
        if nums[0] == 0: return MAX_val
        first = nums[0]
        result = MAX_val
        if first >= length-1:
            return 1
        else:
            for i in range(1,first+1):
                result = min(result, 1 + self.jump(nums[i:]))
        
        return result

@author: zeminzhang
"""
# We use "last" to keep track of the maximum distance that has been reached
# by using the minimum steps "ret", whereas "curr" is the maximum distance
# that can be reached by using "ret+1" steps. Thus,curr = max(i+A[i]) where 0 <= i <= last.
class Solution(object):
    def jump(self, A):    
        ret = 0
        last = 0
        curr = 0
        for i in range(len(A)):
            if i > last:
                last = curr
                ret += 1
            curr = max(curr, i+A[i])
        return ret

sol = Solution()
print sol.jump([5,6,5,3,9,8,3,1,2,8,2,4,8,3,9,1,0,9,4,6,5,9,8,7,4,2,1,0,2])            
            
            
            