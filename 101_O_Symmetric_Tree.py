# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 22:36:06 2016

@author: zeminzhang
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def dfs(p1,p2):
            if p1 and p2:
                if p1 != p2: return False
                else: return dfs(p1.left, p2.right) and dfs(p1.right, p2.left)
            elif not p1 and not p2:
                return True
            else:
                return False
        if not root: return True
        else:
            return dfs(root.left, root.right)
                