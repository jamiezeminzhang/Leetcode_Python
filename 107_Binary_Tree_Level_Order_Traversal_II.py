# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 22:32:15 2016

107. Binary Tree Level Order Traversal II My Submissions Question
Total Accepted: 68632 Total Submissions: 208524 Difficulty: Easy
Given a binary tree, return the bottom-up level order traversal of its nodes' 
values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]

@author: zeminzhang
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None: return []
        
        def dfs(level, root):
            if root:
                if level >= len(res):
                    res.append([])
                res[level].append(root.val)
                dfs(level+1, root.left)
                dfs(level+1, root.right)
            else:
                return
        res = []
        dfs(0, root)
        res.reverse()
        return res