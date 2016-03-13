# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 02:13:05 2016

145. Binary Tree Postorder Traversal My Submissions Question

Total Accepted: 87771 Total Submissions: 254292 Difficulty: Hard
Given a binary tree, return the postorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [3,2,1].

**************************** Postorder: left, right, root **************

题意：实现后序遍历。递归实现比较简单，非递归实现。

解题思路：这道题的迭代求解比先序遍历和后序遍历要麻烦一些。假设一棵树是这样的：

　　　　　　　　　　　　　　　　　　　　　　　　1

　　　　　　　　　　　　　　　　　　　　　　　/　　\

　　　　　　　　　　　　　　　　　　　　　　2　　　　3

　　　　　　　　　　　　　　　　　　　　　　　　　　/　\

　　　　　　　　　　　　　　　　　　　　　　　　　 4　　5

使用一个栈。分几个步骤：
一，将根节点入栈，并将根节点的孩子入栈，入栈顺序为：先入右孩子，再入左孩子，顺序不能错。
因为这样在弹栈时的顺序就是后序遍历的顺序了。如果左孩子还有左孩子或者右孩子，
那么继续按先右后左的顺序入栈。那么上面这棵树开始的入栈顺序是：1，3，2。由于2不存在左右孩子，停止入栈。
二，由于2没有左右孩子，遍历2并将2弹出，同时使用prev记录下2这个节点。
三，2出栈后，栈为{1，3}，此时3在栈顶，由于3存在左右孩子，按顺序入栈，此时栈为{1，3，5，4}。
四，将4和5遍历并出栈，此时prev指向5，栈为{1，3}。prev的作用是什么呢？
用来判断prev是否为栈顶元素的孩子，如果是，则说明子树的孩子已经遍历完成，
需要遍历树根了。以上树为例：4和5出栈后，prev指向5，而5是栈顶元素3的孩子，
说明孩子已经遍历完毕，则遍历3然后弹出3即可，即完成了子树{3，4，5}的后序遍历。
五，此时栈为{1}，为树根，而左右子树都遍历完了，最后遍历树根并弹出即可。
       
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        stack, list = [], []
        prev = None
        if root:
            stack.append(root)
            while stack:
                curr = stack[-1]
                if ( curr.left == None and curr.right == None ) or \
                (prev and (prev == curr.left or prev == curr.right)):
                    list.append(curr.val)
                    prev = curr
                    stack.pop()
                else:
                    if curr.right: stack.append(curr.right)
                    if curr.left: stack.append(curr.left)
        else:
            return []
        
        return list

@author: zeminzhang
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def dfs(root):
            if root:
                dfs(root.left)
                dfs(root.right)
                lis.append(root.val)
            else:
                return
        lis = []
        dfs(root)
        return lis