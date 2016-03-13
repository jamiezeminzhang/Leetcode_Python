# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 00:57:03 2016

104. Maximum Depth of Binary Tree My Submissions Question
Total Accepted: 118466 Total Submissions: 252176 Difficulty: Easy
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root 
node down to the farthest leaf node.

@author: zeminzhang
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(level, root, res):
            if root:
                if level > res[0]: 
                    res[0] = level
                dfs(level+1, root.left, res)
                dfs(level+1, root.right,res)
        res = [0]
        dfs(1, root, res)
        return res[0]
                

sol = Solution()
print sol.maxDepth(TreeNode(0))