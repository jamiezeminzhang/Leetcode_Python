# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 03:08:52 2016

113. Path Sum II My Submissions Question
Total Accepted: 70654 Total Submissions: 255550 Difficulty: Medium
Given a binary tree and a sum, find all root-to-leaf paths where each path's 
sum equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
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
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        def dfs(root, sum, res):
            if root:
                if not root.left and not root.right:
                    if root.val == sum:
                        res.append(root.val)
                        ans.append(res)
                else:
                    dfs(root.left, sum-root.val, res + [root.val])
                    dfs(root.right,sum-root.val, res + [root.val])
            else:
                return
        ans = []
        dfs(root, sum, [])
        return ans