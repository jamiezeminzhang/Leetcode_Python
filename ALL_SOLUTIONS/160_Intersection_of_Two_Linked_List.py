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

my idea: compute the length first,
then start at the position which has the same length towards the end.


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
        headA = dummy1.next; headB = dummy2.next
        if dif > 0:
            dif = abs(dif)
            while dif>0:
                headA = headA.next
                dif -= 1
            while headA:
                if headA == headB:
                    return headA
                else:
                    headA = headA.next
                    headB = headB.next
        else:
            dif = abs(dif)
            while dif>0:
                headB = headB.next
                dif -= 1
            while headA:
                if headA == headB:
                    return headA
                else:
                    headA = headA.next
                    headB = headB.next
        return None