# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 18:19:36 2016

307. Range Sum Query - Mutable

Total Accepted: 6724 Total Submissions: 39886 Difficulty: Medium

Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

The update(i, val) function modifies nums by updating the element at index i to val.
Example:
Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8
Note:
The array is only modifiable by the update function.
You may assume the number of calls to update and sumRange function is distributed evenly.

The given solution is using binary indexed tree (Fenwick Tree)：
http://bookshadow.com/weblog/2015/11/18/leetcode-range-sum-query-mutable/
https://www.hrwhisper.me/binary-indexed-tree-fenwick-tree/

*** Another solution: ***
Using Segmentation Tree
http://bookshadow.com/weblog/2015/08/13/segment-tree-set-1-sum-of-given-range/

class NumArray(object):
    
    # Let's define a segmentation tree first Jamie!
    def initST(self, start, end , s_index):
        if start == end:
            self.st[s_index] = self.nums[start]
        else:
            mid = (start + end)/2
            self.st[s_index] = self.initST(start, mid, 2*s_index+1) + \
            self.initST(mid+1,end,2*s_index+2)
        return self.st[s_index]
    
    # Update the segmentation tree given the s_index and diff
    def updateST(self, start, end, i, diff, s_index):
        if i<start or i>end:
            return
        self.st[s_index] += diff
        if start!=end:
            mid = (start+end)/2
            self.updateST(start, mid, i, diff, s_index*2+1)
            self.updateST(mid+1, end, i, diff, s_index*2+2)
            
    # Compute the sume in the range
    def sumrangeST(self, start, end, qs, qe, s_index):
        
        # 如果当前节点存储的线段是区间的一部分，
        # 返回当前线段的和
        if start>=qs and end <= qe:
            return self.st[s_index]
        # 如果节点存储的线段不在给定区间之内
        if end < qs or start > qe:
            return 0
        # 如果节点的线段与区间的一部分有交集
        mid = (start+end)/2
        return self.sumrangeST(start, mid, qs, qe, s_index*2+1) + \
        self.sumrangeST(mid+1, end, qs, qe, s_index*2+2)
        
            
    def __init__(self, nums):

        self.nums = nums
        self.size = size = len(nums)
        h = int(math.ceil(math.log(size,2))) if size else 0
        maxSize = 2**(h+1) - 1
        self.st = [0]*maxSize
        if size:
            self.initST(0, size-1, 0)
        

    def update(self, i, val):

        if i<0 or i>=self.size:
            return
        diff = val - self.nums[i]
        self.nums[i] = val
        self.updateST(0, self.size-1, i, diff, 0)

    def sumRange(self, i, j):

        if i<0 or j<0 or i>=self.size or j >=self.size:
            return 0
        return self.sumrangeST(0, self.size-1, i, j, 0)
        


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.update(1, 10)
# numArray.sumRange(1, 2)

@author: Jamie
"""

class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        #print 'initial'
        self.nums = nums
        self.sums = [0]*(len(nums)+1)
        self.n = len(nums)
        for i in xrange(self.n):
            self.add(i+1, nums[i])

    def add(self, i, x):
        #print 'add'
        while i <= self.n:
            self.sums[i] += x
            i += self.lowbit(i)
            
    def lowbit(self, x):
        return x&-x
        
    def sum(self,i):
        #print 'sum'
        res = 0
        while i>0:
            res += self.sums[i]
            i -= self.lowbit(i)
        return res
        
    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        self.add(i+1, val-self.nums[i])
        self.nums[i] = val

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        if not self.nums:
            return 0
        else:
            return self.sum(j+1) - self.sum(i)


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.update(1, 10)
# numArray.sumRange(1, 2)