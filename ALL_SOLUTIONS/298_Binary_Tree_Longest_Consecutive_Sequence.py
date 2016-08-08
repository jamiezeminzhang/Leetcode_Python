# -*- coding: utf-8 -*-
"""
Created on Aug 6 2016 9:49 AM

298. Binary Tree Longest Consecutive Sequence

Total Accepted: 11465
Total Submissions: 30345
Difficulty: Medium

Given a binary tree, find the length of the longest consecutive sequence path.

The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The longest consecutive path need to be from parent to child (cannot be the reverse).

For example,
   1
    \
     3
    / \
   2   4
        \
         5
Longest consecutive sequence path is 3-4-5, so return 3.
   2
    \
     3
    / 
   2    
  / 
 1
Longest consecutive sequence path is 2-3,not3-2-1, so return 2.

@author: zzhang
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        self.max_length = 0
        def dfs(node, cur_length):
            if cur_length > self.max_length: 
                self.max_length = cur_length
            if node.left:
                if node.left.val - node.val == 1:
                    dfs(node.left, cur_length+1)
                else:
                    dfs(node.left, 1)
            if node.right:
                if node.right.val - node.val == 1:
                    dfs(node.right, cur_length+1)
                else:
                    dfs(node.right, 1)
        dfs(root, 1)
        return self.max_length
