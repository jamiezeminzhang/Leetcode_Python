# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 00:51:19 2016

103. Binary Tree Zigzag Level Order Traversal My Submissions Question
Total Accepted: 52959 Total Submissions: 190341 Difficulty: Medium
Given a binary tree, return the zigzag level order traversal of its nodes' 
values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]

class Solution(object):
    def zigzagLevelOrder(self, root):
        if not root: return[]
        stack = [root]
        res = []
        
        while stack:
            curr_num_nodes = len(stack)
            curr_res = []
            curr_lvl = len(res)
            next_lvl_nodes = []
            
            while curr_num_nodes>0:
                curr_num_nodes -= 1
                node = stack.pop(0)
                curr_res.append(node.val)
                if node.left: next_lvl_nodes.append(node.left)
                if node.right:next_lvl_nodes.append(node.right)
                
            if curr_lvl % 2 == 0:
                res.append(curr_res)
            else:
                res.append(curr_res[::-1])
                
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
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def dfs(level, direction, root):
            if root:
                if level >= len(res):
                    res.append([])
                if direction == 0:
                    res[level].append(root.val)
                if direction == 1:
                    res[level].insert(0,root.val)
                if root.left:
                    dfs(level+1, (direction+1)%2, root.left)
                if root.right:
                    dfs(level+1, (direction+1)%2, root.right)
        res = []
        dfs(0,0,root)
        return res