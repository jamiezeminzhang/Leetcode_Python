# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 14:50:19 2016

327. Count of Range Sum

Total Accepted: 2853 Total Submissions: 11862 Difficulty: Hard

Given an integer array nums, return the number of range sums that lie in [lower, upper] inclusive.
Range sum S(i, j) is defined as the sum of the elements in nums between indices i and j (i ≤ j), inclusive.

Note:
A naive algorithm of O(n2) is trivial. You MUST do better than that.

Example:
Given nums = [-2, 5, -1], lower = -2, upper = 2,
Return 3.
The three ranges are : [0, 0], [2, 2], [0, 2] and their respective sums are: -2, -1, 2.

***** Solution I *******

和315可以当做同一类题

O(n * logn)解法：
解法I 树状数组（Fenwick Tree）：

1. 预处理前n项和数组sums

2. 将sums数组离散化（排序+去重）得到数组osums

3. 遍历sums，记sumi = sums[i]
   用二分查找得到[sumi - upper, sumi - lower]的离散化下标[left, right]
   用树状数组统计范围[left, right]内的元素个数，并累加至最终结果ans
   若lower <= sumi <= upper，额外地令ans+1
   将sumi的离散化下标记入树状数组
上述算法将题目转化为下面的问题：

对于数组sums中的每一个元素sumi，统计出现在sumi左侧，并且数值在[sumi - upper, sumi - lower]范围内的元素个数。
这就等价于统计区间和[0, i]，[1, i]... [i - 1, i]当中所有落在范围[lower, upper]之内的区间个数。

***** Solution II *****
解法II 归并排序（Merge Sort）：

参考思路：https://leetcode.com/discuss/79083/share-my-solution

First compute the prefix sums: first[m] is the sum of the first m numbers.
Then the sum of any subarray nums[i:k] is simply first[k] - first[i].
So we just need to count those where first[k] - first[i] is in [lower,upper].

To find those pairs, I use mergesort with embedded counting. The pairs in the left half and 
the pairs in the right half get counted in the recursive calls. We just need to also count the 
pairs that use both halves.

For each left in first[lo:mid] I find all right in first[mid:hi] so that right - left lies in 
[lower, upper]. Because the halves are sorted, these fitting right values are a subarray first[i:j]. 
With increasing left we must also increase right, meaning must we leave out first[i] if it's too 
small and and we must include first[j] if it's small enough.

Besides the counting, I also need to actually merge the halves for the sorting. I let sorted do
 that, which uses Timsort and takes linear time to recognize and merge the already sorted halves.

def countRangeSum(self, nums, lower, upper):
    first = [0]
    for num in nums:
        first.append(first[-1] + num)
    def sort(lo, hi):
        mid = (lo + hi) / 2
        if mid == lo:
            return 0
        count = sort(lo, mid) + sort(mid, hi)
        i = j = mid
        for left in first[lo:mid]:
            while i < hi and first[i] - left <  lower: i += 1
            while j < hi and first[j] - left <= upper: j += 1
            count += j - i
        first[lo:hi] = sorted(first[lo:hi])
        return count
    return sort(0, len(first))
    
@author: Jamie
"""

class FenwickTree(object):
    def __init__(self, n):
        self.sums = [0]*(n+1)
        self.size = n
    
    def lowbit(self, x):
        return x&-x
    
    def add(self, i, val):
        while i <= self.size:
            self.sums[i] += val
            i+=self.lowbit(i)
            
    def sum(self, i):
        res = 0
        while i>0:
            res += self.sums[i]
            i -= self.lowbit(i)
        return res
        
class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        sums = nums[:]
        for i in range(1,len(sums)):
            sums[i] += sums[i-1]
        osums = sorted(set(sums))
        ft = FenwickTree(len(sums))
        ans = 0
        for x in sums:
            left  = bisect.bisect_left(osums, x-upper)
            right = bisect.bisect_right(osums, x-lower)
            ans += ft.sum(right) - ft.sum(left) + ( lower<=x<=upper)
            ft.add(bisect.bisect_right(osums, x), 1)   # Using bisect_right!!!
        return ans