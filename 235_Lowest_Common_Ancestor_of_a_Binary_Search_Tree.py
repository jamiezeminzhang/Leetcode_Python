# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 12:42:08 2016

235. Lowest Common Ancestor of a Binary Search Tree My Submissions Question
Total Accepted: 54365 Total Submissions: 142952 Difficulty: Easy
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two 
nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to 
be a descendant of itself).”

        _______6______
       /              \
    ___2__          ___8__
   /      \        /      \
   0      _4       7       9
         /  \
         3   5
For example, the lowest common ancestor (LCA) of nodes 2 and 8 is 6. Another example is LCA of nodes 
2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

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
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def dfs(node, p, q):
            if node.val > p.val and node.val > q.val:
                return dfs(node.left, p, q)
            elif node.val < p.val and node.val <q.val:
                return dfs(node.right, p, q)
            else:
                return node
        
        return dfs(root, p, q)