# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 21:35:31 2016

92. Reverse Linked List II

Total Accepted: 62693 Total Submissions: 231141 Difficulty: Medium

Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 ≤ m ≤ n ≤ length of list.

@author: zeminzhang
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution(object):
    def reverseBetween(self, head, m, n):
        if not head or not head.next: return head
        dummy = ListNode('s'); dummy.next = head
        d = dummy
        for i in range(m-1):
            d = d.next
        head1 = d.next
        for i in range(n-m):
            temp = d.next
            d.next = head1.next
            head1.next = head1.next.next
            d.next.next = temp
        return dummy.next
        
