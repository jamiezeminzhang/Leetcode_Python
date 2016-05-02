# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 23:53:00 2016

42. Trapping Rain Water

Total Accepted: 65452 Total Submissions: 202906 Difficulty: Hard


Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

For example, 
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.

*** Another solution:

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


*** 复制两个数组nums1和nums2
*** 从左往右扫，nums1[i] = 到目前i为止遇到的最大值。
*** 从右往左扫，nums2[i] = 到目前i为止遇到的最大值。
*** 然后再扫一遍nums1，nums1 = min( nums1[i], nums2[i] )。此时的nums1就是填满水后的样子。
*** return sum(nums1) - sum(height)
*** 时间复杂度O(n)。空间复杂度O(n)。

@author: zeminzhang
"""
# my own solution
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        nums1, nums2 = height[:], height[:]
        max1, max2 = 0, 0
        for i in range(len(nums1)):
            max1 = max(max1, nums1[i])
            nums1[i] = max1
        for i in range(len(nums2)-1,-1,-1):
            max2 = max(max2, nums2[i])
            nums2[i] = max2
        for i in range(len(nums1)):
            nums1[i] = min( nums1[i], nums2[i])
        return sum(nums1) - sum(height)
        