# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 18:41:39 2016

295. Find Median from Data Stream My Submissions Question

Total Accepted: 11092 Total Submissions: 51886 Difficulty: Hard
Median is the middle value in an ordered integer list. If the size of the list is even, 
there is no middle value. So the median is the mean of the two middle value.

Examples: 
[2,3,4] , the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.
For example:

add(1)
add(2)
findMedian() -> 1.5
add(3) 
findMedian() -> 2

解题思路：
维护大顶堆（MaxHeap） + 小顶堆（MinHeap）

需要满足下面的约束条件：

大顶堆中存储的元素 均不大于 小顶堆中的元素
MaxHeap.size() == MinHeap.size()，或者 MaxHeap.size() == MinHeap.size() + 1
则有：

当MaxHeap.size() == MinHeap.size() + 1时，中位数就是MaxHeap的堆顶元素
当MaxHeap.size() == MinHeap.size()时，中位数就是MaxHeap堆顶元素与MinHeap堆顶元素的均值
使用Python的内置堆算法heapq可以很容易地实现小顶堆，而大顶堆可以通过对元素的值 * -1实现。

**堆插入和删除都是O(logn) ****

另外一个红黑树的解法
https://leetcode.com/discuss/82402/both-o-log-n-red-black-tree-solution-in-python

和bisect的解法
https://leetcode.com/discuss/65142/pythons-bisect-module-o-n-add-and-o-1-return-median

@author: Jamie
"""

from heapq import *
class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.minHeap = []
        self.maxHeap = []
        

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        heappush(self.maxHeap, -num)
        max_top = -self.maxHeap[0] if self.maxHeap else None
        min_top = self.minHeap[0] if self.minHeap else None
        if min_top < max_top or len(self.maxHeap)>len(self.minHeap)+1:
            heappush( self.minHeap, -heappop(self.maxHeap) )
        if len(self.maxHeap) < len(self.minHeap):
            heappush( self.maxHeap, -heappop(self.minHeap) )
 
    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        if len(self.maxHeap) == len(self.minHeap):
            return 1.0*(self.minHeap[0]-self.maxHeap[0])/2
        else:
            return -self.maxHeap[0]

# Your MedianFinder object will be instantiated and called as such:
# mf = MedianFinder()
# mf.addNum(1)
# mf.findMedian()