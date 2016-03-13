# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 23:14:40 2016

109. Convert Sorted List to Binary Search Tree My Submissions Question

Total Accepted: 62287 Total Submissions: 210172 Difficulty: Medium
Given a singly linked list where elements are sorted in ascending order, 
convert it to a height balanced BST.

61%

@author: zeminzhang
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        val_list = []
        p = head
        while p:
            val_list.append(p.val)
            p = p.next
        length = len(val_list)
        if length == 0: return None
        if length == 1: return TreeNode(val_list[0])
        if length == 2:
            root = TreeNode(val_list[1])
            root.left = TreeNode(val_list[0])
            return root
        def dfs(start, end):
            if end - start < 0: return None
            mid = (start+end)/2
            root = TreeNode(val_list[mid])
            root.left = dfs(start,mid-1)
            root.right = dfs(mid+1,end)
            return root
        return dfs(0,length-1)
            
            