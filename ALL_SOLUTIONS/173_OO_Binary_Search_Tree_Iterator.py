# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 15:11:56 2016

173. Binary Search Tree Iterator My Submissions Question

Total Accepted: 40213 Total Submissions: 121281 Difficulty: Medium
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.

解题思路：
维护一个栈，从根节点开始，每次迭代地将根节点的左孩子压入栈，直到左孩子为空为止。

调用next()方法时，弹出栈顶，如果被弹出的元素拥有右孩子，则以右孩子为根，将其左孩子迭代压栈。

另请参阅：https://oj.leetcode.com/discuss/20001/my-solutions-in-3-languages-with-stack


@author: Jamie
"""

# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        self.pushLeft(root)
    
    def pushLeft(self, node):
        while node:
            self.stack.append(node)
            node = node.left
        
    def hasNext(self):
        """
        :rtype: bool
        """
        return self.stack

    def next(self):
        """
        :rtype: int
        """
        top = self.stack.pop()
        self.pushLeft(top.right)
        return top.val

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())