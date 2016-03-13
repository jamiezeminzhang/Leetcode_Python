# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 00:07:23 2016

82. Remove Duplicates from Sorted List II My Submissions Question

Total Accepted: 63733 Total Submissions: 243150 Difficulty: Medium
Given a sorted linked list, delete all nodes that have duplicate numbers, 
leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if head == None or head.next == None:
            return head
        dummy = ListNode(0); dummy.next = head
        p = dummy
        tmp = dummy.next
        while p.next:
            while tmp.next and tmp.next.val == p.next.val:
                tmp = tmp.next
            if tmp == p.next:
                p = p.next
                tmp = p.next
            else:
                p.next = tmp.next
        return dummy.next
        

@author: zeminzhang
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None: return head
        if head.val == head.next.val and head.next.next==None: return None
        
        dummy = ListNode('#')
        dummy.next = head
        p = dummy
        while p.next:
#            print p.val
            tmp = p
            while tmp.next and tmp.next.next:
                if tmp.next.next != None:
                    if tmp.next.val != tmp.val and tmp.next.val != tmp.next.next.val:
                        p.next = tmp.next
                        p = p.next
                        break
                    else:
                        tmp = tmp.next
            if tmp.next.next == None:
                if tmp.next.val == tmp.val:
                    p.next = None
                    break
                else:
                    p.next = tmp.next
                    break
            
        return dummy.next
        
a = ListNode(1)
a.next = ListNode(1)
a.next.next = ListNode(2)

sol = Solution()
b = sol.deleteDuplicates(a)

while b:
    print b.val
    b = b.next
