# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 07:15:40 2016

199. Binary Tree Right Side View

Total Accepted: 34128 Total Submissions: 104014 Difficulty: Medium

Given a binary tree, imagine yourself standing on the right side of it, 
return the values of the nodes you can see ordered from top to bottom.

For example:
Given the following binary tree,
   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
You should return [1, 3, 4].

*** My solution: Same idea as P102
***
@author: Jamie
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def dfs(level, root):
            if root:
                if level == len(res):
                    res.append(0)
                res[level] = root.val
                if root.left: dfs(level+1, root.left)
                if root.right: dfs(level+1, root.right)
        res = []
        dfs(0,root)
        return res