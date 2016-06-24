# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 21:46:10 2016

86. Partition List

Total Accepted: 57882 Total Submissions: 201557 Difficulty: Medium

Given a linked list and a value x, partition it such that all nodes less than 
x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.

@author: zeminzhang
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head or not head.next: return head
        dummy1, dummy2 = ListNode('#'), ListNode('#')
        p1, p2, dummy1.next = dummy1, dummy2, head
        while p1.next:
            if p1.next.val >= x:
                p2.next = p1.next
                p2 = p2.next
                if p1.next.next:p1.next = p1.next.next
                else: p1.next = None
            else:
                p1 = p1.next
        p1.next, p2.next = dummy2.next, None
        return dummy1.next
                
        