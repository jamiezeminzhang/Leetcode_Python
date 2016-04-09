# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 04:33:05 2016

148. Sort List 

Total Accepted: 63805 Total Submissions: 265468 Difficulty: Medium
Sort a linked list in O(n log n) time using constant space complexity.


=== Below is the recursion result, which is wrong ===
=== Since you always need stacks to save previous recursion results===
class Solution(object):
            
    def merge2(self, p1, p2):
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
        
    def sortList(self, head):
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



*** Given is the correct bottom up solution

@author: zeminzhang
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: return head
        dummy = ListNode('s'); dummy.next = head; tmp = head
        length = 0
        while tmp:
            tmp = tmp.next
            length += 1
        step = 1
        while step<length:
            cur, tail = dummy.next, dummy
            while cur:
                left = cur
                right = self.split(left,step)
                cur = self.split(right, step)
                tail = self.merge2(left,right,tail)
            step <<= 1
        return dummy.next
        
    # merge 2 sorted lists, and append the result to head
    # return the tail
    def merge2(self, p1, p2, head):
        dummy = ListNode('#');p = dummy
        while p1 and p2:
            if p1.val <= p2.val:
                p.next = p1
                p1 = p1.next; p = p.next
            else:
                p.next = p2
                p2 = p2.next; p = p.next
        p.next = p1 or p2
        head.next = dummy.next
        while p.next: p = p.next
        return p
    
    # divide the linked list into two lists
    # first linked list contains n nodes
    # return the head of second linked list
    def split(self, head, n):
        for i in range(n-1): 
            if head: head = head.next
            else: break
        if not head: return None
        second = head.next
        head.next = None
        return second

        
        