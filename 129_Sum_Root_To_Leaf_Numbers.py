# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 01:40:41 2016

@author: zeminzhang
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root,s):
            if root:
                s += str(root.val)
                if root.left:
                    dfs(root.left, s)
                if root.right:
                    dfs(root.right,s)
                if not root.left and not root.right:
                    res.append(int(s))
        res = []
        dfs(root,'')
        return sum(res)

sol = Solution()
a = TreeNode(0)
a.left = TreeNode(1)
a.right = TreeNode(2)
print sol.sumNumbers(a)