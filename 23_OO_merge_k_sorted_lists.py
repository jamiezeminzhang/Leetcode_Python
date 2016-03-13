# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 14:02:38 2015

LeetCode #23 Merge k Sorted Lists

Merge k sorted linked lists and return it as one sorted list. 
Analyze and describe its complexity. 

@author: zzhang
"""
import heapq
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode[]} lists
    # @return {ListNode}
    def mergeKLists(self, lists):
          
        heap = []
        for node in lists:
            if node:
                heap.append((node.val,node))
                
        heapq.heapify(heap)
        
        head = ListNode(0); curr = head
        while heap:
            pop = heapq.heappop(heap)
            curr.next = ListNode(pop[0])
            curr = curr.next
            if pop[1].next:
                heapq.heappush(heap,(pop[1].next.val , pop[1].next))
        return head.next
        
        
        
sol = Solution();
a = ListNode(0);
a.val = 1
b = ListNode(0);
b.val = 0
c = sol.mergeKLists([a,b])
while c:
    print c.val
    c = c.next
        
        
        