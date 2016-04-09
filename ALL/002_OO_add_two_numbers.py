# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 14:15:25 2015

LeetCode #2 Add two numbers

You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8


@author: zzhang
"""

# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        carry = 0
        res = None
        res_end = None
        while l1 is not None or l2 is not None or carry == 1:
            temp = 0
            if l1 is not None:
                temp += l1.val
                l1 = l1.next
            if l2 is not None:
                temp += l2.val
                l2 = l2.next
            temp += carry
            digit = temp % 10
            carry = temp / 10
            if res is None:
                res = ListNode(digit)
                res_end = res
            else:
                res_end.next = ListNode(digit)
                res_end = res_end.next
        return res