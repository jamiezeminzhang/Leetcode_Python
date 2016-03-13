# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 06:15:39 2016

164. Maximum Gap My Submissions Question

Total Accepted: 28392 Total Submissions: 108849 Difficulty: Hard
Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

Try to solve it in linear time/space.

Return 0 if the array contains less than 2 elements.

You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.


***
那么，线性的排序算法有哪些？计数排序、基数排序、桶排序。
下面用桶排序实现，这也是leetcode上给出的参考解法，我直接copy过来：

Suppose there are N elements and they range from A to B.

Then the maximum gap will be no smaller than ceiling[(B - A) / (N - 1)]

Let the length of a bucket to be len = ceiling[(B - A) / (N - 1)], then we will have at most 
num = (B - A) / len + 1 of bucket

for any number K in the array, we can easily find out which bucket it belongs by calculating 
loc = (K - A) / len and therefore maintain the maximum and minimum elements in each bucket.

Since the maximum difference between elements in the same buckets will be at most len - 1, 
so the final answer will not be taken from two elements in the same buckets.

For each non-empty buckets p, find the next non-empty buckets q, then q.min - p.max could be the 
potential answer to the question. Return the maximum of all those values.

@author: Jamie
"""

class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length <2: return 0
        if length == 2: return abs(nums[0]-nums[1])
        min_val, max_val = 2**32-1, -1
        for num in nums:
            min_val = num if num<min_val else min_val
            max_val = num if num>max_val else max_val
            
        bucket_length = math.ceil(max_val - min_val)/(length-1)
        if bucket_length == 0: return 0
#        print bucket_length
        num_bucket = int( (max_val-min_val)/bucket_length + 1)
#        print num_bucket
        max_bucket = [[] for x in range(num_bucket)]
        min_bucket = [[] for x in range(num_bucket)]
        
        for num in nums:
            id = int( (num-min_val)/bucket_length )
            if not max_bucket[id]:
                max_bucket[id].append(num)
                min_bucket[id].append(num)
            else:
                if num>max_bucket[id][0]:
                    max_bucket[id][0] = num
                if num<min_bucket[id][0]:
                    min_bucket[id][0] = num
        res = max_bucket[0][0] - min_bucket[0][0]
        prev, i = 0, 1
        while i < length:
            if not max_bucket[i]: 
                i += 1
            else:
                res = max(res, min_bucket[i][0]-max_bucket[prev][0] )
                prev = i
                i += 1
        return res
            
sol = Solution()
print sol.maximumGap([3,6,9,1])
            
            
            