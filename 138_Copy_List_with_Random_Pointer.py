# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 09:06:49 2016

138. Copy List with Random Pointer My Submissions Question
Total Accepted: 57632 Total Submissions: 222707 Difficulty: Hard
A linked list is given such that each node contains an additional random pointer 
which could point to any node in the list or null.

Return a deep copy of the list.

@author: zeminzhang
"""

# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        def dfs(head):
            if not head: return None
            else:
                if head in dic: return dic[head]
                else:
                    tmp = RandomListNode(head.label)
                    dic[head] = tmp
                    tmp.next = dfs(head.next)
                    tmp.random = dfs(head.random)
                    return tmp
        dic = {}
        return dfs(head)
a = RandomListNode(1)
a.next = RandomListNode(2)
a.random = RandomListNode(3)
sol = Solution()
res = sol.copyRandomList(a)
print res.label
print res.next.label
print res.random.label