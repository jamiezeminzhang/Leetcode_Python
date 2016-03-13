# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 04:07:11 2016

114. Flatten Binary Tree to Linked List My Submissions Question
Total Accepted: 72882 Total Submissions: 240709 Difficulty: Medium
Given a binary tree, flatten it to a linked list in-place.

For example,
Given

         1
        / \
       2   5
      / \   \
     3   4   6
The flattened tree should look like:
   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6
click to show hints.

Hints:
If you notice carefully in the flattened tree, each node's right child points 
to the next node of a pre-order traversal.

解题思路：首先将左右子树分别平化为链表，这两条链表的顺序分别为左子树的先序遍历和右子树的先序遍历。
然后将左子树链表插入到根节点和右子树链表之间，就可以了。左右子树的平化则使用递归实现。


@author: zeminzhang
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        if root == None: return
        self.flatten(root.left)
        self.flatten(root.right)
        p = root
        if not p.left: return
        p = p.left
        while p.right:
            p = p.right
        p.right = root.right
        root.right = root.left
        root.left = None
        