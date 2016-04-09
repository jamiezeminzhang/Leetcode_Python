# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 17:23:53 2016

328. Odd Even Linked List My Submissions Question

Total Accepted: 17387 Total Submissions: 46319 Difficulty: Easy
Given a singly linked list, group all odd nodes together followed by the even nodes.
 Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example:
Given 1->2->3->4->5->NULL,
return 1->3->5->2->4->NULL.

Note:
The relative order inside both the even and odd groups should remain as it was in the input. 
The first node is considered odd, the second node even and so on ...

A more concise solution:

class Solution(object):
    def oddEvenList(self, head):
        if not head: return head
        odd, even, evenhead = head, head.next, head.next
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = evenhead
        return head

@author: Jamie
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next or not head.next.next: 
            return head
        dummy = ListNode('#')
        dummy.next = head
        tail = head
        num_nodes = 1
        while tail.next:
            tail = tail.next
            num_nodes += 1
        
        count = 0
        while count<num_nodes/2:
            count += 1
            tmp = head.next
            head.next = head.next.next
            head = head.next
            tail.next = tmp
            tail = tail.next
            tail.next = None
        return dummy.next
                
                