# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 21:46:10 2016

86. Partition List My Submissions Question
Total Accepted: 57882 Total Submissions: 201557 Difficulty: Medium
Given a linked list and a value x, partition it such that all nodes less than 
x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.

@author: zeminzhang
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head is None or head.next is None: return head
        dummy = ListNode('#')
        dummy.next = head
        p = dummy
        count = 0
        # find the last node and count the total number
        while p.next:
            p = p.next
            count += 1
        
        tmp = dummy
        while count > 0 :
            count -= 1
            if tmp.next.val >= x:
                p.next = tmp.next
                p = p.next
                tmp.next = tmp.next.next
            else:
                tmp = tmp.next
        p.next = None
        return dummy.next

sol = Solution()
head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(1)

res = sol.partition(head,2)
while res:
    print res.val
    res = res.next
