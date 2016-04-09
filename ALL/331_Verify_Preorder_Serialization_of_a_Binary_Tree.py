# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 10:11:27 2016

331. Verify Preorder Serialization of a Binary Tree My Submissions Question
Total Accepted: 5401 Total Submissions: 17161 Difficulty: Medium
One way to serialize a binary tree is to use pre-order traversal. When we encounter a non-null node, 
we record the node's value. If it is a null node, we record using a sentinel value such as #.

     _9_
    /   \
   3     2
  / \   / \
 4   1  #  6
/ \ / \   / \
# # # #   # #
For example, the above binary tree can be serialized to the string "9,3,4,#,#,1,#,#,2,#,6,#,#",
 where # represents a null node.

Given a string of comma separated values, verify whether it is a correct preorder traversal 
serialization of a binary tree. Find an algorithm without reconstructing the tree.

Each comma separated value in the string must be either an integer or a character '#' representing null pointer.

You may assume that the input format is always valid, for example it could never contain two consecutive 
commas such as "1,,3".

Example 1:
"9,3,4,#,#,1,#,#,2,#,6,#,#"
Return true

Example 2:
"1,#"
Return false

Example 3:
"9,#,#,1"
Return false

My Solution

class Solution(object):
    def isValidSerialization(self, preorder):
        pre = preorder.split(',')
        pre_pre = []
        while len(pre_pre) != len(pre):
            pre_pre = pre
            i = 0
            while i < len(pre)-2:
                if pre[i]!='#' and pre[i+1:i+3] == ['#','#']:
                    pre[i] = '#'
                    pre = pre[:i+1]+pre[i+3:]
                i+=1
            
        if pre == ['#']:
            return True
        else:
            return False
            
@author: Jamie
"""

class Solution(object):
    def isValidSerialization(self, preorder):
        need = 1
        for val in preorder.split(','):
            if not need:
                return False
            print val
            print ' #'.find(val)
            need -= ' #'.find(val)
            print need
        return not need
sol = Solution()
#print sol.isValidSerialization("9,9,9,9,#,#,9,9,9,9,#,#,9,#,9,#,#,#,#,9,9,9,#,#,#,9,#,9,#,#,#")
print sol.isValidSerialization('9,#,#')