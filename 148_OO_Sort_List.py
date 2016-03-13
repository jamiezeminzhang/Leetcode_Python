# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 04:33:05 2016

148. Sort List My Submissions Question

Total Accepted: 63805 Total Submissions: 265468 Difficulty: Medium
Sort a linked list in O(n log n) time using constant space complexity.

@author: zeminzhang
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        


class Solution(object):
            
    def merge2(self, p1, p2):
        """
        merge 2 sorted list
        """
        if not p1: return p2
        if not p2: return p1
        dummy = ListNode('#');
        p = dummy
        while p1 and p2:
            if p1.val <= p2.val:
                p.next = p1
                p1 = p1.next; p = p.next
            else:
                p.next = p2
                p2 = p2.next; p = p.next
        if not p1: p.next = p2
        elif not p2: p.next = p1
        return dummy.next
        
    def sortList2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: return head
        fast, slow = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        p1 = head;p2 = slow.next
        slow.next = None
        p1 = self.sortList(p1)
        p2 = self.sortList(p2)
        head = self.merge2(p1,p2)
        return head

sol = Solution()
head = ListNode(2); head.next = ListNode(1)
#head2 = ListNode(1.5); head2.next = ListNode(3)
#head.next.next = head2
sol.sortList2(head)
print head.val
print head.next
        
        