# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 21:20:35 2016

141. Linked List Cycle My Submissions Question
Total Accepted: 92028 Total Submissions: 250102 Difficulty: Medium
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?

My solution: AC but need to change the list

class Solution(object):
    def hasCycle(self, head):
        while head:
            if head.val == '#':
                return True
            else:
                head.val = '#'
                head = head.next if head.next else None
        return False

题意：判断链表中是否存在环路。

解题思路：快慢指针技巧，slow指针和fast指针开始同时指向头结点head，fast每次走两步，
slow每次走一步。如果链表不存在环，那么fast或者fast.next会先到None。如果链表中存在环路，
则由于fast指针移动的速度是slow指针移动速度的两倍，所以在进入环路以后，两个指针迟早会相遇，
如果在某一时刻slow==fast，说明链表存在环路。
@author: zeminzhang
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow: return True
        return False