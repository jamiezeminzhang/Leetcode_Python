# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 20:35:44 2016
117. Populating Next Right Pointers in Each Node II My Submissions Question
Total Accepted: 54853 Total Submissions: 168360 Difficulty: Hard
Follow up for problem "Populating Next Right Pointers in Each Node".

What if the given tree could be any binary tree? Would your previous solution still work?

Note:

You may only use constant extra space.
For example,
Given the following binary tree,
         1
       /  \
      2    3
     / \    \
    4   5    7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \    \
    4-> 5 -> 7 -> NULL

# Why my solution is not correct at first !!!

 ========= @connect(root.right)should be the first!!! ==============

A more concise version:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if root:
            if root.left and root.right:
                root.left.next = root.right
                tmp = root.next
                while tmp:
                    if tmp.left: root.right.next = tmp.left; break
                    if tmp.right: root.right.next = tmp.right; break
                    tmp = tmp.next
            elif root.left:
                tmp = root.next
                while tmp:
                    if tmp.left: root.left.next = tmp.left; break
                    if tmp.right: root.left.next = tmp.right; break
                    tmp = tmp.next
            elif root.right:
                tmp = root.next
                while tmp:
                    if tmp.left: root.right.next = tmp.left; break
                    if tmp.right: root.right.next = tmp.right; break
                    tmp = tmp.next
            self.connect(root.right)
            self.connect(root.left)
            # @connect(root.right)should be the first!!!

@author: zeminzhang
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if root:
            if root.left:
                if root.right:
                    root.left.next = root.right
                else:
                    if root.next:
                        p = root.next
                        while p and not p.left and not p.right:
                            p = p.next
                        if p:
                            if p.left:
                                root.left.next = p.left
                            elif not p.left and p.right:
                                root.left.next = p.right
            if root.right:
                if root.next:
                    p = root.next
                    while p and not p.left and not p.right:
                        p = p.next
                    if p:
                        if p.left:
                            root.right.next = p.left
                        elif not p.left and p.right:
                            root.right.next = p.right
            self.connect(root.left)
            self.connect(root.right)