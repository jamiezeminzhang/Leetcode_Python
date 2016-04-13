# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 09:22:10 2016
206. Reverse Linked List

Total Accepted: 83499 Total Submissions: 219371 Difficulty: Easy

Reverse a singly linked list.

click to show more hints.

Hint:
A linked list can be reversed either iteratively or recursively. Could you implement both?

***
基本想法：head不动。每次将head后面的node提到dummy后面，head.next=head.next.next，直到head.next == None

** Recursive one **

class Solution(object):
    def reverseList(self, head):
        return self._reverse(head, None)

    def _reverse(self, node, prev):
        if not node:
            return prev
        n = node.next
        node.next = prev
        return self._reverse(n, node)


@author: Jamie
"""

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
			
        dummy = ListNode('s')
        dummy.next = head
        while head.next:
            tmp = dummy.next
            dummy.next = head.next
            head.next = head.next.next
            dummy.next.next = tmp
        return dummy.next

head = ListNode(1)
head.next = ListNode(2)
sol = Solution()
res = sol.reverseList(head)
while res:
    print res.val
    res = res.next
