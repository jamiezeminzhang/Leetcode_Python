# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 23:37:35 2016

102. Binary Tree Level Order Traversal My Submissions Question
Total Accepted: 87109 Total Submissions: 276765 Difficulty: Easy
Given a binary tree, return the level order traversal of its nodes' values. 
(ie, from left to right, level by level).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]

Iterative solution:

class Solution(object):
    def levelOrder(self, root):
        if not root: return []
        stack = [root]
        curr_level = 0
        res = []
        
        while stack:
            cur_lvl_nodes = len(stack)
            cur_lvl_res = []
            next_lvl_nodes = []
            while cur_lvl_nodes>0:
                cur_lvl_nodes -= 1
                node = stack.pop(0)
                cur_lvl_res.append(node.val)
                if node.left: next_lvl_nodes.append(node.left)
                if node.right:next_lvl_nodes.append(node.right)
            res.append(cur_lvl_res)
            stack = next_lvl_nodes
        return res
		
@author: zeminzhang
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def dfs(level, root):
            if root:
                if level >= len(res):
                    res.append([])
                res[level].append(root.val)
                if root.left:
                    dfs(level+1, root.left)
                if root.right:
                    dfs(level+1, root.right)
                        
        res = []
        dfs(0,root)
        return res