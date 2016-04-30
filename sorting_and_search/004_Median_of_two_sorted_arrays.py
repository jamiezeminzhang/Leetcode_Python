# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 14:26:03 2015

LeetCode #4: Median of Two Sorted Arrays

There are two sorted arrays nums1 and nums2 of size m and n respectively. 
Find the median of the two sorted arrays. 
The overall run time complexity should be O(log (m+n)).


*** 至于为什么谁大留谁 ***

----(k/2)个----- a ----------
----(k/2)个----- b ----------

如果a<b，那么kth一定不在第一列的a前面。
因为kth如果在a前面，说明在下面数列里比kth小的有多于k/2个。但是比b (b>a) 小的都没有那么多，矛盾。

*** 至于为什么谁空留谁 ***
考虑 [4]， [1,2,3,5,6,7] 选第4个

*** 加上a is not None 是因为如果 a is None那么自动 a<b。但是a is None应该在下面的条件中。


@author: zzhang
"""
class Solution:
    # @param {integer[]} nums1
    # @param {integer[]} nums2
    # @return {float}
    def findMedianSortedArrays(self, nums1, nums2):
        n = len(nums1)+len(nums2)
        if n %2 == 1:
            return self.findKth(nums1,nums2,n/2+1)
        else:
            smaller = self.findKth(nums1,nums2,n/2)
            larger = self.findKth(nums1,nums2,n/2+1)
            return (smaller+larger)/2.0
        
    def findKth(self,nums1,nums2,k):
        if len(nums1) == 0:
            return nums2[k-1]
        if len(nums2) == 0:
            return nums1[k-1]
        if k == 1:
            return min(nums1[0],nums2[0])
            
        a = nums1[k/2-1] if len(nums1) >= k/2 else None
        b = nums2[k/2-1] if len(nums2) >= k/2 else None
        
        if b is None or (a is not None and a<b):  # 谁大留谁。
            return self.findKth(nums1[k/2:],nums2,k-k/2)
        return self.findKth(nums1,nums2[k/2:],k-k/2)
        