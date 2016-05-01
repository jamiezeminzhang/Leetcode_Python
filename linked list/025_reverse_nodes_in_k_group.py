# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 15:23:33 2015

LeetCode # 25: Reverse Nodes in k-Group

 Given a linked list, reverse the nodes of a linked list k at a time 
 and return its modified list.

If the number of nodes is not a multiple of k then left-out nodes in the 
end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5 

@author: zzhang
"""

# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next: return head
        
        dummy = ListNode('#')
        dummy.next = head
        start, end = dummy, head
        
        while end:
            for i in xrange(k-1):
                if end: end = end.next
                else: return dummy.next
            if not end: return dummy.next
            for i in xrange(k-1):
                tmp = end.next
                end.next = start.next
                start.next = start.next.next
                end.next.next = tmp
            for i in xrange(k):
                end = end.next
                start = start.next
        return dummy.next

