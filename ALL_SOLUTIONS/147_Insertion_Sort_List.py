# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 04:32:12 2016

147. Insertion Sort List

Total Accepted: 63806 Total Submissions: 223635 Difficulty: Medium

Sort a linked list using insertion sort.

@author: zeminzhang
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: return head
        
        dummy = ListNode('s'); dummy.next = head
        cur = head.next; dummy.next.next = None; p = dummy
        
        while cur:
            if cur.val < p.val: p = dummy # 不加这个判断会超时。只有当新值比当前point的值小的时候才重置pointer
            while p.next and p.next.val<cur.val: p = p.next
            p.next, cur.next, cur = cur, p.next, cur.next
        return dummy.next
            
        
        
        
        