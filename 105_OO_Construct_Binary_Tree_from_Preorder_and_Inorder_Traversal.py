# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 06:56:27 2016

105. Construct Binary Tree from Preorder and Inorder Traversal

Total Accepted: 54930 Total Submissions: 198014 Difficulty: Medium
Given preorder and inorder traversal of a tree, construct the binary tree.

################

Given version is the correct version of recursion one.
https://leetcode.com/discuss/83521/python-recursion-version-iteration-version-easy-understand

A iterative version which beats 100%:
# From @JieGhost
class Solution(object):
    def buildTree(self, preorder, inorder):
        if len(preorder) == 0:
            return None

        head = TreeNode(preorder[0])
        stack = [head]
        i = 1
        j = 0

        while i < len(preorder):
            temp = None
            t = TreeNode(preorder[i])
            while stack and stack[-1].val == inorder[j]:
                temp = stack.pop()
                j += 1
            if temp:
                temp.right = t
            else:
                stack[-1].left = t
            stack.append(t)
            i += 1

        return head
        
@author: zeminzhang
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    preorder = []
    inorder = []
    def buildTree(self, preorder, inorder):
	    """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        self.preorder = preorder
        self.inorder = inorder
        return self.dfs(0, len(self.preorder), 0, len(self.inorder))

    def dfs(self, pre_start, pre_end, in_start, in_end): # [start, end)
        if pre_end - pre_start <= 0:
            return None
        root = TreeNode(self.preorder[pre_start])
        offset = self.inorder[in_start : in_end+1].index(self.preorder[pre_start])
        root.left = self.dfs(pre_start+1, pre_start+1+offset, in_start, in_start+offset)
        root.right = self.dfs(pre_start+1+offset, pre_end, in_start+1+offset, in_end)
        return root