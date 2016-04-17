# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 14:09:54 2016

236. Lowest Common Ancestor of a Binary Tree

Total Accepted: 33643 Total Submissions: 117820 Difficulty: Medium

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between 
two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a 
node to be a descendant of itself).”

        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2       0       8
         /  \
         7   4
For example, the lowest common ancestor (LCA) of nodes 5 and 1 is 3. Another example is LCA of 
nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

@author: Jamie
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        Solution.node = None
        def dfs(root, p, q):
            if not root: return 0
            else:
                res = dfs(root.left,p,q)+dfs(root.right,p,q) + (root == p or root == q)
                if res == 2 and not Solution.node:
                    Solution.node = root
                return res
        dfs(root,p,q)
        return Solution.node