# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 21:23:13 2016

142. Linked List Cycle II My Submissions Question
Total Accepted: 66630 Total Submissions: 211694 Difficulty: Medium
Given a linked list, return the node where the cycle begins. If there is no 
cycle, return null.

Note: Do not modify the linked list.

Follow up:
Can you solve it without using extra space?

http://www.cnblogs.com/zuoyuan/p/3701877.html
在fast指针和slow指针相遇后，fast指针不动，slow指针回到head，然后slow指针和fast指针
同时向前走，只不过这一次两个指针都是一步一步向前走。两个指针相遇的节点就是环路的起点。

@author: zeminzhang
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None: return None
        slow,fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        if slow == fast:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
        return None