# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 21:35:31 2016

92. Reverse Linked List II My Submissions Question
Total Accepted: 62693 Total Submissions: 231141 Difficulty: Medium
Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 ≤ m ≤ n ≤ length of list.


This is the online solution, which beats 41%

class Solution(object):
    def reverseBetween(self, head, m, n):
        if not head or not head.next: return head
        dummy = ListNode('s'); dummy.next = head
        d = dummy
        for i in range(m-1):
            d = d.next
        head1 = d.next
        for i in range(n-m):
            temp = d.next
            d.next = head1.next
            head1.next = head1.next.next
            d.next.next = temp
        return dummy.next
        
        
@author: zeminzhang
"""

# My solution only beats 0.34%...
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m==n: return head
        count = n-m
        dummy = ListNode('#')
        dummy.next=head
        head = dummy
        while m>1:
            head = head.next
            m-=1
        p1 = head.next
        p2 = dummy.next
        while n>1:
            p2 = p2.next
            n -= 1
        while count>0:
            count -= 1
            head.next = p1.next # connect to p2
            p1.next = p2.next # p1.next = p2.next= None
            p2.next = p1 # p2.next = p1
            p1 = head.next
        return dummy.next

sol = Solution()
head = ListNode(3)
head.next = ListNode(5)
a = sol.reverseBetween(head,1,2)
print 'Result:'
while a:
    print a.val
    a = a.next