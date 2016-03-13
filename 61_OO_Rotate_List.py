# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 03:21:23 2016

Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.

@author: zeminzhang
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 0 : return head
        if head is None: return None
        
        length = 0
        dummy = ListNode(0)
        dummy.next = head
        p = dummy
        while p.next:
            p = p.next
            length += 1
        p.next = dummy.next
        step = length - k%length
        for i in range(step):
            p = p.next
        head = p.next
        p.next = None
        return head
        