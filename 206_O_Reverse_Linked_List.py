# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 09:22:10 2016
206. Reverse Linked List My Submissions Question

Total Accepted: 83499 Total Submissions: 219371 Difficulty: Easy
Reverse a singly linked list.

click to show more hints.

Hint:
A linked list can be reversed either iteratively or recursively. Could you implement both?

***
Remeber to remove the next of head! Otherwise it will be a circle.

** Recursive one **

class Solution(object):
    def reverseList(self, head):     
        def rev(head):
            if not head.next:
                return (head, head)
            elif not head.next.next:
                p1 = head.next
                p1.next = head
                head.next = None
                return (p1,p1.next)
            else:
                tmp = rev(head.next)
                tmp[1].next = head
                head.next = None
                return (tmp[0], head)
        
        if not head or not head.next: return head
        res = rev(head)
        return res[0]


@author: Jamie
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: return head
        dummy = ListNode('#')
        dummy.next = head
        p1, p2 = head.next, head
        while p1:
            tmp = p1.next
            p1.next = p2
            p2 = p1
            p1 = tmp
        dummy.next.next = None
        return p2

head = ListNode(1)
head.next = ListNode(2)
sol = Solution()
res = sol.reverseList(head)
while res:
    print res.val
    res = res.next
