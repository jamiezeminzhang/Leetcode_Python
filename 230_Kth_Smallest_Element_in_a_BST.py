# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 09:07:45 2016

230. Kth Smallest Element in a BST My Submissions Question
Total Accepted: 36444 Total Submissions: 101281 Difficulty: Medium
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note: 
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest 
frequently? How would you optimize the kthSmallest routine?

@author: Jamie
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        Solution.ans = -1
        def dfs(root, lis):
            if Solution.ans!=-1: return
            if root:
                dfs(root.left, lis)
                lis.append(root.val)
                if len(lis) == k: Solution.ans = root.val
                dfs(root.right, lis)
            else:
                return
        dfs(root,[])
        return Solution.ans