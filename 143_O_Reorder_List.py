# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 01:27:31 2016

143. Reorder List

Total Accepted: 58695 Total Submissions: 264365 Difficulty: Medium

Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You must do this in-place without altering the nodes' values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.


@author: zeminzhang
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next or not head.next.next:
            return
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        head1, head2 = head, slow.next
        slow.next = None
        
        # Reverse list2
        dummy = ListNode('#')
        dummy.next = head2; tmp = head2.next; head2.next= None
        while tmp:
            tmp2 = dummy.next; dummy.next= tmp
            tmp = tmp.next; dummy.next.next= tmp2
        head2 = dummy.next
        
        # Combine list1 and list2
        p1 = head1; p2 = head2
        while p2:
            tmp1 = p1.next; p1.next = p2
            tmp2 = p2.next; p2.next = tmp1
            p1 = tmp1
            p2 = tmp2
            
            
head = ListNode(1)
head.next = ListNode(2); head.next.next = ListNode(3)
sol = Solution()
sol.reorderList(head)
while head:
    print head.val
    head = head.next        