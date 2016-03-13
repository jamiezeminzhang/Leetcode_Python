# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 09:58:25 2016

257. Binary Tree Paths My Submissions Question

Total Accepted: 35437 Total Submissions: 130935 Difficulty: Easy
Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

["1->2->5", "1->3"]

@author: Jamie
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root: return []
        
        def dfs(root, lis):
            # not leaf
            if root and (root.left or root.right):
                if root.left: dfs(root.left, lis + [str(root.val)])
                if root.right: dfs(root.right, lis+ [str(root.val)])
            elif root:
                ans.append(lis+[str(root.val)])
            else:
                return
        
        ans = []
        dfs(root,[])
        res = []
        for i in ans:
            res.append('->'.join(i))
        return res