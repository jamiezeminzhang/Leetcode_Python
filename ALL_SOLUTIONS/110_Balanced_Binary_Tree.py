# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 01:25:01 2016

110. Balanced Binary Tree My Submissions Question
Total Accepted: 94528 Total Submissions: 283797 Difficulty: Easy
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in 
which the depth of the two subtrees of every node never differ by more than 1.

@author: zeminzhang
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        else: return self.isBalanced(root.left) and self.isBalanced(root.right) \
        and abs(self.depth(root.left)-self.depth(root.right))<=1
    
    def depth(self, root):
        if not root: return 0
        else: return max(self.depth(root.left), self.depth(root.right))+1
            
        
        