# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 05:29:37 2016

95. Unique Binary Search Trees II My Submissions Question
Total Accepted: 48708 Total Submissions: 169236 Difficulty: Medium
Given n, generate all structurally unique BST's (binary search trees) 
that store values 1...n.

For example,
Given n = 3, your program should return all 5 unique BST's shown below.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.


OJ's Binary Tree Serialization:
The serialization of a binary tree follows a level order traversal, where '#' 
signifies a path terminator where no node exists below.

Here's an example:
   1
  / \
 2   3
    /
   4
    \
     5
The above binary tree is serialized as "{1,2,3,#,#,4,#,#,5}".

@author: zeminzhang
"""

#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        
        def dfs(start, n):
            if n == 0: return []
            if n == 1: return [TreeNode(start)]
            if n == 2: 
                a = TreeNode(start); a.right = TreeNode(start+1)
                b = TreeNode(start+1); b.left = TreeNode(start)
                return [a,b]
            res = []
            for i in range(start,n+start):
                if i == start:
                    dp_tmp = dfs(start+1,n-1)
                    for j in dp_tmp:
                        tmp = TreeNode(i)
                        tmp.right = j
                        res.append(tmp)
                if i >start and i < n+start-1:
                    dp_tmp1 = dfs(start,i-start)
                    dp_tmp2 = dfs(i+1,n+start-1-i)
                    for j1 in dp_tmp1:
                        for j2 in dp_tmp2:
                            tmp = TreeNode(i)
                            tmp.left = j1
                            tmp.right = j2
                            res.append(tmp)
                if i == n+start-1:
                    dp_tmp = dfs(start,n-1)
                    for j in dp_tmp:
                        tmp = TreeNode(i)
                        tmp.left = j
                        res.append(tmp)
            return res
            
        return dfs(1,n)
        
                

