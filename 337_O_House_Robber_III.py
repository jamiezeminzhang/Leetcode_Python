# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 22:30:49 2016

337. House Robber III My Submissions Question
Total Accepted: 131 Total Submissions: 513 Difficulty: Medium
The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:
     3
    / \
   2   3
    \   \ 
     3   1
Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
Example 2:
     3
    / \
   4   5
  / \   \ 
 1   3   1
Maximum amount of money the thief can rob = 4 + 5 = 9.
@author: Jamie

*** My own solution: TLE

*** Right way of dfs: make it return a tuple (a1, a2), which is the max with/without the node value

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node):
            if not node:
                return (0, 0)
            (l1,l2) = dfs(node.left)
            (r1,r2) = dfs(node.right)
            return (node.val+l2+r2, max(l1+r1,l1+r2,l2+r1,l2+r2) )

        return max( dfs(root) )