# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 21:36:29 2016

83. Remove Duplicates from Sorted List

Total Accepted: 98185 Total Submissions: 273256 Difficulty: Easy

Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.


@author: zeminzhang
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None: return head
        dummy = ListNode('#')
        dummy.next = head
        p = head
        while p.next != None:
            if p.next.val == p.val:
                p.next = p.next.next
            else:
                p = p.next
        return dummy.next