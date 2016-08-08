# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 23:53:00 2016

42. Trapping Rain Water

Total Accepted: 65452 Total Submissions: 202906 Difficulty: Hard


Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

For example, 
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.

*** 复制两个数组nums1和nums2
*** 从左往右扫，nums1[i] = 到目前i为止遇到的最大值。
*** 从右往左扫，nums2[i] = 到目前i为止遇到的最大值。
*** 然后再扫一遍nums1，nums1 = min( nums1[i], nums2[i] )。此时的nums1就是填满水后的样子。
*** return sum(nums1) - sum(height)
*** 时间复杂度O(n)。空间复杂度O(n)。

@author: zeminzhang
"""

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        h1, h2 = [0], [0]
        for h in height:
            h1.append(max(h, h1[-1]))
        for h in height[::-1]:
            h2.append(max(h, h2[-1]))
        h1, h2 = h1[1:], h2[::-1][:-1]
        hh = [min(h1[i], h2[i]) for i in range(len(height))]
        return sum(hh)-sum(height)
        