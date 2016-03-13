# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 22:57:16 2016

108. Convert Sorted Array to Binary Search Tree My Submissions Question
Total Accepted: 66250 Total Submissions: 183184 Difficulty: Medium
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

#### a faster solution ####
always use the indices if possible instead of the whole list

class Solution:
    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, num):
        return self.createBST(num, 0, len(num) - 1)
     
    def createBST(self, num, start, end):
        if start > end: return None
        mid = (start + end) / 2
        root = TreeNode(num[mid])
        root.left = self.createBST(num, start, mid - 1)
        root.right = self.createBST(num, mid + 1, end)
        return root

@author: zeminzhang
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def BST(nums):
            length = len(nums)
            if length == 0: return None
            if length == 1: return TreeNode(nums[0])
            if length == 2: 
                root = TreeNode(nums[1])
                root.left = TreeNode(nums[0])
                return root
            mid = length/2
            root = TreeNode(nums[mid])
            root.left = BST(nums[:mid])
            root.right = BST(nums[mid+1:])
            return root
        return BST(nums)