# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 02:21:12 2016

111. Minimum Depth of Binary Tree My Submissions Question
Total Accepted: 91313 Total Submissions: 303491 Difficulty: Easy
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root 
node down to the nearest leaf node.


61.14%
@author: zeminzhang
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        else:
            if not root.left and not root.right: return 1
            elif not root.left and root.right: 
                return 1 + self.minDepth(root.right)
            elif root.left and not root.right:
                return 1 + self.minDepth(root.left)
            else:
                return 1+min(self.minDepth(root.left), self.minDepth(root.right))