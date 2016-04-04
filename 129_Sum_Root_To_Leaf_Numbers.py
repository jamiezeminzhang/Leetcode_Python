# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 01:40:41 2016

129. Sum Root to Leaf Numbers

Total Accepted: 73158 Total Submissions: 225538 Difficulty: Medium

Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

For example,

    1
   / \
  2   3
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.

Return the sum = 12 + 13 = 25.

@author: zeminzhang
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root,s):
            if root:
                s += str(root.val)
                if root.left:
                    dfs(root.left, s)
                if root.right:
                    dfs(root.right,s)
                if not root.left and not root.right:
                    res.append(int(s))
        res = []
        dfs(root,'')
        return sum(res)

sol = Solution()
a = TreeNode(0)
a.left = TreeNode(1)
a.right = TreeNode(2)
print sol.sumNumbers(a)