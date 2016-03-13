# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 11:44:59 2016

234. Palindrome Linked List My Submissions Question

Total Accepted: 38026 Total Submissions: 141329 Difficulty: Easy
Given a singly linked list, determine if it is a palindrome.

Follow up:
Could you do it in O(n) time and O(1) space?


1). 使用快慢指针寻找链表中点

2). 将链表的后半部分就地逆置，然后比对前后两半的元素是否一致

3). 恢复原始链表的结构（可选）


@author: Jamie
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next: return True
        
        p1, p2 = head, head
        while p2.next and p2.next.next:
            p1 = p1.next
            p2 = p2.next.next
        p = p1.next

        dummy = ListNode('#')
        dummy.next = p
        while p.next:
            tmp = dummy.next
            dummy.next = p.next
            p.next = p.next.next
            dummy.next.next = tmp
        
        p1_new, p2_new = head, dummy.next
        while p2_new:
            if p1_new.val == p2_new.val:
                p1_new = p1_new.next
                p2_new = p2_new.next
            else:
                return False
        return True