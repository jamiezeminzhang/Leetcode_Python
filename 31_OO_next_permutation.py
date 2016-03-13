# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 15:46:01 2015

LeetCode # 31: Next Permutation

 Implement next permutation, which rearranges numbers into the 
 lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the 
lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its 
corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1


解题思路：输出字典序中的下一个排列。比如123生成的全排列是：123，132，213，231，312，321。
那么321的next permutation是123。下面这种算法据说是STL中的经典算法。
在当前序列中，从尾端往前寻找两个相邻升序元素，升序元素对中的前一个标记为partition。
然后再从尾端寻找另一个大于partition的元素，并与partition指向的元素交换，
然后将partition后的元素（不包括partition指向的元素）逆序排列。
比如14532，那么升序对为45，partition指向4，由于partition之后除了5没有比4大的数，
所以45交换为54，即15432，然后将partition之后的元素逆序排列，即432排列为234，
则最后输出的next permutation为15234。确实很巧妙。

@author: zzhang
"""

class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def nextPermutation(self, nums):
        if len(nums) != 0 and len(nums) != 1:
            LenNum = len(nums)
            i = LenNum-1
            while i>=0:
                if nums[i-1]>=nums[i]:
                    i -= 1
                if nums[i-1] < nums[i]:
                    break
            if i == 0:
                nums.reverse()
            else:
                for k in range(LenNum-1,i-1,-1):
                    if nums[k]>nums[i-1]:
                        nums[i-1],nums[k] = nums[k],nums[i-1]
                        break
                left = i
                right = LenNum-1
                while left<right:
                    nums[left],nums[right] = nums[right],nums[left]
                    left += 1
                    right -= 1
        
a = [1,3,2]
sol = Solution()
sol.nextPermutation(a)
print a
