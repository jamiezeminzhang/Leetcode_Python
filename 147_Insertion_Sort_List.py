# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 04:32:12 2016

147. Insertion Sort List My Submissions Question

Total Accepted: 63806 Total Submissions: 223635 Difficulty: Medium
Sort a linked list using insertion sort.

@author: zeminzhang
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return None
        dummy = ListNode('#'); dummy.next = ListNode(head.val)

        p = head.next
        while p:
            p1 = dummy.next; p1_prev = dummy
            if p.val <= p1.val:
                dummy.next = ListNode(p.val)
                dummy.next.next = p1
                p = p.next
            else:
                while p1 and p.val > p1.val:
                    p1_prev = p1
                    p1 = p1.next
                if not p1: 
                    p1_prev.next = ListNode(p.val)
                    p1_prev.next.next = None
                    p = p.next
                else:
                    p1_prev.next = ListNode(p.val)
                    p1_prev.next.next = p1
                    p = p.next
        return dummy.next
        
        
        
        