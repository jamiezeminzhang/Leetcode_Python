# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 19:23:14 2016

297. Serialize and Deserialize Binary Tree My Submissions Question

Total Accepted: 13261 Total Submissions: 49776 Difficulty: Medium

Serialization is the process of converting a data structure or object into a sequence of bits so 
that it can be stored in a file or memory buffer, or transmitted across a network connection link 
to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your 
serialization/deserialization algorithm should work. You just need to ensure that a binary tree can 
be serialized to a string and this string can be deserialized to the original tree structure.

For example, you may serialize the following tree

    1
   / \
  2   3
     / \
    4   5
as "[1,2,3,null,null,4,5]", just the same as how LeetCode OJ serializes a binary tree. You do not 
necessarily need to follow this format, so please be creative and come up with different approaches yourself.
Note: Do not use class member/global/static variables to store states. Your serialize and deserialize 
algorithms should be stateless.

@author: Jamie
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        self.max_lvl = 0
        def dfs_lvl(root,lvl):
            if root:
                self.max_lvl = max(self.max_lvl,lvl)
                dfs_lvl(root.left, lvl+1)
                dfs_lvl(root.right,lvl+1)
            else:
                return
        dfs_lvl(root,0)
        
        node = root
        res = ['']*(self.max_lvl+1)
        def dfs(node, level):
            if node:
                if node.val!='#' and level != self.max_lvl:
                    if not node.left: node.left = TreeNode('#')
                    if not node.right:node.right = TreeNode('#')
                res[level] += '~'+str(node.val) if res[level] else str(node.val)
                dfs(node.left,  level+1)
                dfs(node.right, level+1)
            else:
                return
        dfs(node,0)
        return '~'.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data: return None
        data = data.split('~')
        node_lis = [TreeNode(data[0])]
        root = node_lis[0]
        
        data = data[1:]
        while data:
            new_node_lis = []
            while node_lis:
                node = node_lis.pop(0)
                left = TreeNode(data.pop(0))
                if left.val != '#':
                    node.left = left
                    new_node_lis.append(left)
            
                right= TreeNode(data.pop(0))
                if right.val != '#':
                    node.right = right
                    new_node_lis.append(right)
                
            node_lis = new_node_lis
        return root
                

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))