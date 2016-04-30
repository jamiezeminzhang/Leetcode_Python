# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 10:11:27 2016

331. Verify Preorder Serialization of a Binary Tree

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

*** My Solution ****
*** 对于每种类似于 '1','#','#'的叶子节点，把这个叶子节点直接变成'#'，并且删去后面的空节点
*** 循环到最后，合法的先序序列必然会变成['*']

class Solution(object):
    def isValidSerialization(self, preorder):
        pre = preorder.split(',')
        stack = []
        for i in pre:
            stack.append(i)
            while len(stack)>2 and stack[-2]==stack[-1]=='#':
                if stack[-3]=='#': return False
                stack.pop(); stack.pop()
                stack[-1]='#'
        return stack == ['#']
@author: Jamie
"""

# 首先定义 need = 1
# 每次遇到非空节点就在need上+1
# 每次遇到空节点'#'就在need上-1
# 没到末尾之前，任何时候need=0说明空节点过多。false。
# 到末尾发现need没有等于0，说明空节点和非空节点不匹配。false。
# 最后return true
class Solution(object):
    def isValidSerialization(self, preorder):
        need = 1
        for val in preorder.split(','):
            if not need:
                return False
            need -= ' #'.find(val)
        return not need

		