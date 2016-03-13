# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 22:24:54 2016

100. Same Tree My Submissions Question
Total Accepted: 107546 Total Submissions: 252393 Difficulty: Easy
Given two binary trees, write a function to check if they are equal or not.

Two binary trees are considered equal if they are structurally identical and
 the nodes have the same value.

@author: zeminzhang
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p and q:
            return self.isSameTree(p.left,q.left) and p.val == q.val and self.isSameTree(p.right,q.right)
        elif (p and not q) or (q and not p):
            return False
        else:
            return True