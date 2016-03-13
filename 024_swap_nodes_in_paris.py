# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 14:39:39 2015

LeetCode # 24: Swap Nodes in Pairs

 Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values 
in the list, only nodes itself can be changed. 

@author: zzhang
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def swapPairs(self, head):
        if not head:
            return []
        if not head.next:
            return head

        dummy = ListNode(0)
        dummy.next = head
        p = dummy

        while p.next:
            if not p.next.next:
                return dummy.next
            else:
                q = ListNode(p.next.next.val)
                p.next.next = p.next.next.next
                q.next= p.next 
                p.next = q
                p = p.next.next
        return dummy.next