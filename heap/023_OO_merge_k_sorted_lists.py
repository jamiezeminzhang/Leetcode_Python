# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 14:02:38 2015

LeetCode #23 Merge k Sorted Lists

Merge k sorted linked lists and return it as one sorted list. 
Analyze and describe its complexity. 

@author: zzhang
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = []
        for node in lists:
            if node: heapq.heappush(heap,(node.val, node))
            
        dummy = ListNode('#'); head = dummy
        while heap:
            pop = heapq.heappop(heap)
            head.next = ListNode(pop[0])
            head = head.next
            if pop[1].next:
                heapq.heappush(heap, ( pop[1].next.val, pop[1].next ))
        return dummy.next
        
        
        
        
        
        