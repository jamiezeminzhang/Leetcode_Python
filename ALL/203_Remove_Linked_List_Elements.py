# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 09:02:29 2016

203. Remove Linked List Elements My Submissions Question

Total Accepted: 51398 Total Submissions: 185053 Difficulty: Easy
Remove all elements from a linked list of integers that have value val.

Example
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5

@author: Jamie
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = ListNode('#')
        dummy.next = head; prev = dummy
        while head:
            if head.val == val:
                prev.next = head.next
                head = head.next
            else:
                prev = prev.next
                head = head.next
        return dummy.next
                