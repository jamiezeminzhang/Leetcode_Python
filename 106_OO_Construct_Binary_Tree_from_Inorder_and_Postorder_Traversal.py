# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 22:01:55 2016
106. Construct Binary Tree from Inorder and Postorder Traversal
Total Accepted: 51584 Total Submissions: 179894 Difficulty: Medium

Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

*** Iterative Solution ***
class Solution(object):
    def buildTree(self, inorder, postorder):
        oi, pi = 0,0
        stack = []
        cur = None
        while pi < len(postorder):
            if len(stack) and stack[-1].val == postorder[pi]:
                stack[-1].right = cur
                cur = stack.pop()
                pi += 1
            else:
                stack.append(TreeNode(inorder[oi]))
                stack[-1].left = cur
                cur = None
                oi += 1
        return cur
@author: zeminzhang
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        length = len(inorder)
        if length == 0: return None
        
        def dfs(in_start, in_end, post_start, post_end):
            if in_end-in_start < 0:
                return None
            root = TreeNode(postorder[post_end])
            root_idx = inorder[in_start:in_end+1].index(postorder[post_end])
            root.left  = dfs(in_start, in_start + root_idx-1, post_start, post_start + root_idx -1 )
            root.right = dfs(in_start+root_idx+1, in_end, post_start+root_idx, post_end-1 )
            return root
            
        return dfs(0,length-1,0,length-1)
            
sol = Solution()
a = sol.buildTree([-1],[-1])
print a.val