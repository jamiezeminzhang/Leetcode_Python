# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 12:22:20 2016

222. Count Complete Tree Nodes My Submissions Question

Total Accepted: 27235 Total Submissions: 112831 Difficulty: Medium
Given a complete binary tree, count the number of nodes.

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes 
in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the 
last level h.

一个非常巧妙的dfs算法

如果当前子树的“极左节点”（从根节点出发一路向左）与“极右节点”（从根节点出发一路向右）的高度h相同，则当前子树为满二叉树，返回2^h - 1

否则，递归计算左子树与右子树的节点个数。
class Solution(object):
    def countNodes(self, root):
        def dfs(root):
            if not root: return 0
            l,r = root, root
            lvl_l, lvl_r = 0,0
            while l:                
                l = l.left; lvl_l += 1
            while r:
                r = r.right; lvl_r += 1
            if lvl_l == lvl_r: return 2**lvl_r - 1
            else: return dfs(root.left) + dfs(root.right) + 1
        return dfs(root)


*** 我的算法是递归算最后一层的node数， 只打败了1.4%的人，但是可以AC
算最后一层的node数也可以用这个方法
http://bookshadow.com/weblog/2015/06/06/leetcode-count-complete-tree-nodes/

只需要二分枚举第h层的节点个数即可。
将第h层的节点从0至2^h - 1依次编号（根节点的层数记为0）
若用0表示左孩子，1表示右孩子，则这些编号的二进制形式是从根节点出发到叶子节点的“路径”。
例如高度为2，包含6个节点的完全二叉树：

Lv0        1 
         /    \
Lv1     2      3
       /  \   /  \
Lv2   4   5  6   -

No.   00  01 10
从1号节点（根节点）出发，到第5号节点的路径为01（左右），同时该节点为第2层的第2个节点。

@author: Jamie
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
            
        node1, node2 = root, root
        lvl_left, lvl_right = 0, 0
        while node1.left:
            node1 = node1.left;  lvl_left+=1
        while node2.right:
            node2 = node2.right; lvl_right += 1
            
        if lvl_left == lvl_right: return 2**(lvl_left+1)-1
        Solution.res = 0
        Solution.flag = False
        def dfs(root, level):
            if Solution.flag: return
            if level == lvl_left: 
                Solution.res += 1
                return
            else:
                if not root.left: 
                    Solution.flag = True
                    return 
                elif not root.right:
                    Solution.res +=1
                    Solution.flag = True
                    return
                else:
                    dfs(root.left,level+1)
                    dfs(root.right,level+1)
        dfs(root, 0)
        return 2**(lvl_right+1)-1 + Solution.res