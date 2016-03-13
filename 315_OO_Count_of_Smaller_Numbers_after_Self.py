# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 15:21:13 2016

315. Count of Smaller Numbers After Self My Submissions Question

Total Accepted: 6106 Total Submissions: 21183 Difficulty: Hard
You are given an integer array nums and you have to return a new counts array. 
The counts array has the property where counts[i] is the number of smaller 
elements to the right of nums[i].

Example:

Given nums = [5, 2, 6, 1]

To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
Return the array [2, 1, 1, 0].

**** 解法I 树状数组 （Binary Indexed Tree / Fenwick Tree）：
1. 对原数组nums进行离散化处理（排序+去重），将nums从实数范围映射到 [1, len(set(nums))]，记得到的新数组为iNums

2. 从右向左遍历iNums，对树状数组的iNums[i]位置执行+1操作，然后统计(0, iNums[i])的区间和

也可以用线段树，代码从略。


**** 解法II 二叉搜索树 （Binary Search Tree）：
树节点TreeNode记录下列信息：

元素值：val
小于该节点的元素个数：leftCnt
节点自身的元素个数：cnt
左孩子：left
右孩子：right
从右向左遍历nums，在向BST插入节点时顺便做统计

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.leftcnt = 0
        self.cnt = 1
        self.left = None
        self.right = None

class BST(object):
    def __init__(self):
        self.root = None
    
    def insert(self, val):
        if not self.root:
            self.root = TreeNode(val)
            return 0
            
        root = self.root
        cnt = 0
        while root:
            if val < root.val:
                root.leftcnt += 1
                if not root.left:
                    root.left = TreeNode(val)
                    break
                root = root.left
            elif val > root.val:
                cnt += root.leftcnt + root.cnt
                if not root.right:
                    root.right = TreeNode(val)
                    break
                root = root.right
            else:
                cnt += root.leftcnt
                root.cnt += 1
                break
        return cnt


class Solution(object):
    def countSmaller(self, nums):
        t = BST()
        ans = [0]*len(nums)
        for i in range(len(nums)-1,-1,-1):
            ans[i] = t.insert(nums[i])
        return ans

**** 解法III 非常非常非常聪明的解法 *******

The smaller numbers on the right of a number are exactly those that jump from 
its right to its left during a stable sort. So I do mergesort with added tracking 
of those right-to-left jumps.

class Solution(object):
    def countSmaller(self, nums):
        def sort(enum):
            half = len(enum) / 2
            if half:
                # format of left and right: [(old_index, val),...]
                # from smallest to largest
                left, right = sort(enum[:half]), sort(enum[half:])
                # inverse indices
                for i in range(len(enum))[::-1]:
                    if not right or left and left[-1][1] > right[-1][1]:
                        smaller[left[-1][0]] += len(right)
                        enum[i] = left.pop()
                    else:
                        enum[i] = right.pop()
            return enum
        smaller = [0] * len(nums)
        print sort(list(enumerate(nums)))
        return smaller

@author: zzhang04
"""

class FenwickTree(object):
    def __init__(self, n):
        self.sums = [0]*(n+1)
        self.n = n
    
    def lowbit(self,i):
        return i&-i
    
    def add(self, i, val):
        while i<=self.n:
            self.sums[i]+=val
            i += self.lowbit(i)
    
    def sum(self,i):
        res = 0
        while i>0:
            res += self.sums[i]
            i -= self.lowbit(i)
        return res
    
class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dic = {}
        unique_and_sorted_num = sorted(set(nums))
        for idx, item in enumerate(unique_and_sorted_num):
            dic[item] = idx+1
        new_num = [dic[item] for item in nums]
        ft = FenwickTree(len(new_num))
        ans = [0] * len(new_num)
        for i in range(len(new_num)-1,-1,-1):
            ans[i] = ft.sum(new_num[i]-1)
            ft.add(new_num[i],1)
        return ans