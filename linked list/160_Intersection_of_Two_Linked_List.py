# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 03:23:57 2016

160. Intersection of Two Linked Lists My Submissions Question

Total Accepted: 61819 Total Submissions: 206050 Difficulty: Easy
Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3
begin to intersect at node c1.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.

My idea: compute the length first,
then start at the position which has the same length towards the end.

*** Another solution ***
1. Maintain two pointers pA and pB initialized at the head of A and B, respectively. Then let them both traverse through the lists, one node at a time.
2. When pA reaches the end of a list, then redirect it to the head of B (yes, B, that's right.); similarly when pB reaches the end of a list, redirect it the head of A.
3. If at any point pA meets pB, then pA/pB is the intersection node.

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB: return None
        p1, p2 = headA, headB
        flag1, flag2 = False, False # used for first time p1.next/p2.next is None
        while True:
            if p1 == p2: return p1
            if p1.next: p1 = p1.next
            elif not flag1: 
                p1 = headB
                flag1 = True
            else: return None
            
            if p2.next: p2 = p2.next
            elif not flag2: 
                p2 = headA
                flag2 = True
        return None

@author: zeminzhang
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        length1, length2 = 0, 0
        dummy1, dummy2 = ListNode('#'), ListNode('#')
        dummy1.next = headA; dummy2.next = headB
        while headA:
            headA = headA.next
            length1 += 1
        while headB:
            headB = headB.next
            length2 += 1
        dif = length1-length2
        if dif>0: p1, p2 = dummy1.next, dummy2.next
        else: p2, p1 = dummy1.next, dummy2.next
        for i in range(abs(dif)):
            p1 = p1.next
        while p1:
            if p1==p2: return p1
            else: p1, p2 = p1.next, p2.next

        return None