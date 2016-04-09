# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 21:38:23 2016

98. Validate Binary Search Tree My Submissions Question
Total Accepted: 79524 Total Submissions: 386166 Difficulty: Medium
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Solution:
print out the binary tree and check its order.

*** A better solution ***
def isValidBST(self, root, floor=float('-inf'), ceiling=float('inf')):
    if not root: 
        return True
    if root.val <= floor or root.val >= ceiling:
        return False
    # in the left branch, root is the new ceiling; contrarily root is the new floor in right branch
    return self.isValidBST(root.left, floor, root.val) and self.isValidBST(root.right, root.val, ceiling)
	
	
@author: zeminzhang
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        
        def dfs(root):
            if root:
                dfs(root.left)
                res.append(root.val)
                dfs(root.right)
        res = []
        dfs(root)
        for i in range(len(res)-1):
            if res[i] >= res[i+1]: return False
        return True
        