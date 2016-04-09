# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 22:36:06 2016
101. Symmetric Tree My Submissions Question
Total Accepted: 99255 Total Submissions: 295792 Difficulty: Easy
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.

The given solution is the recursive one.

Here is the iterative one
class Solution(object):
    def isSymmetric(self, root):
        if not root: return True
        stack = [(root.left, root.right)]
        while stack:
            left, right = stack.pop()
            if not left and not right: continue
            if not left or not right: return False
            if left.val == right.val:
                stack.insert(0,(left.left,right.right))
                stack.insert(0,(left.right,right.left))
            else:
                return False
        return True
            
@author: zeminzhang
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def dfs(p1,p2):
            if p1 and p2:
                if p1 != p2: return False
                else: return dfs(p1.left, p2.right) and dfs(p1.right, p2.left)
            elif not p1 and not p2:
                return True
            else:
                return False
        if not root: return True
        else:
            return dfs(root.left, root.right)
                