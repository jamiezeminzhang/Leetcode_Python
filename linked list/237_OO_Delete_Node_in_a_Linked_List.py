# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 14:13:41 2016

237. Delete Node in a Linked List

Total Accepted: 63361 Total Submissions: 144877 Difficulty: Easy

Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.

Supposed the linked list is 1 -> 2 -> 3 -> 4 and you are given the third node with value 3, 
the linked list should become 1 -> 2 -> 4 after calling your function.

***
We only have access to c, but we also have access to d through c.
copy d's value to c, and point c to e.
***


@author: Jamie
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next