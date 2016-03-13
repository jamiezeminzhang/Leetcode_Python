# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 15:23:33 2015

LeetCode # 25: Reverse Nodes in k-Group

 Given a linked list, reverse the nodes of a linked list k at a time 
 and return its modified list.

If the number of nodes is not a multiple of k then left-out nodes in the 
end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5 

@author: zzhang
"""

# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} k
    # @return {ListNode}
    def reverseKGroup(self, head, k):
        if not head:
            return []
        
        dummy = ListNode(0)
        dummy.next = head
        p = dummy
        
        while p.next:
            q = p
            k_list = []
            count = 0
            while count <=k-1:
                if not p.next:
                    return dummy.next
                if p.next:
                    count += 1
                    k_list.append(p.next.val)
                    p = p.next
            k_list.reverse()
            dummy2 = ListNode(0)
            t = dummy2
            for i in k_list:
                t.next = ListNode(i)
                t = t.next
            t.next = p.next
            q.next = dummy2.next
            p = t
        return dummy.next

sol = Solution()

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)
head.next.next.next.next.next.next = ListNode(7)
head.next.next.next.next.next.next.next = ListNode(8)

result = sol.reverseKGroup(head,2)

print result.val
print result.next.val
print result.next.next.val
print result.next.next.next.val
print result.next.next.next.next.val
print result.next.next.next.next.next.val
print result.next.next.next.next.next.next.val
print result.next.next.next.next.next.next.next.val