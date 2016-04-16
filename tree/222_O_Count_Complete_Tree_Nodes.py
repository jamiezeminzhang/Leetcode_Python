# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 12:22:20 2016

222. Count Complete Tree Nodes

Total Accepted: 27235 Total Submissions: 112831 Difficulty: Medium

Given a complete binary tree, count the number of nodes.

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes 
in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the 
last level h.

一个非常巧妙的dfs算法

如果当前子树的“极左节点”（从根节点出发一路向左）与“极右节点”（从根节点出发一路向右）的高度h相同，则当前子树为满二叉树，返回2^h - 1

否则，递归计算左子树与右子树的节点个数。


@author: Jamie
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        def dfs(root):
            if not root: return 0
            l,r = root, root
            lvl_l, lvl_r = 0,0
            while l:                
                l = l.left; lvl_l += 1
            while r:
                r = r.right; lvl_r += 1
            if lvl_l == lvl_r: return 2**lvl_r - 1
            else: return dfs(root.left) + dfs(root.right) + 1
        return dfs(root)