# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 16:15:03 2015

LeetCode # 21 Merge Two Sorted Lists

Merge two sorted linked lists and return it as a new list. 
The new list should be made by splicing together the nodes 
of the first two lists.

@author: zzhang
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def mergeTwoLists(self, l1, l2):
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        
        dummy = ListNode(0)
        p1 = l1
        p2 = l2
        p = dummy
        while p1 != None and p2 != None:
            if p1.value <= p2.value:
                p.next = p1
                p1 = p1.next
                p = p.next
            else:
                p.next = p2
                p2 = p2.next
                p = p.next
        if p1==None:
            p.next = p2
        if p2==None:
            p.next = p1
            
        return dummy.next