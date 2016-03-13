# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 07:14:46 2016

124. Binary Tree Maximum Path Sum My Submissions Question
Total Accepted: 58200 Total Submissions: 255968 Difficulty: Hard
Given a binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting 
node to any node in the tree along the parent-child connections. The path does
 not need to go through the root.

For example:
Given the below binary tree,

       1
      / \
     2   3
Return 6.

＊＊＊题意理解的问题 ！！
＊＊＊起点和终点只要是树里面的节点就可以了

那么思路就是：（左子树中的最大路径和，右子树中的最大路径和，以及左子树中以root.
left为起点的最大路径（需要大于零）+右子树中以root.right为起点的最大路径（需要大于零）+
root.val），这三者中的最大值就是最大的路径和。

@author: zeminzhang
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None: return 0
        Solution.max = -100000000
        self.maxSum(root)
        return Solution.max
    
    def maxSum(self, root): # maximum sum of path starting from root
        if root == None: return 0
        sum = root.val
        lmax, rmax = 0, 0
        if root.left:
            lmax = self.maxSum(root.left) # when we call this we already 
            if lmax > 0: sum += lmax      # updated Solution.max in left subtree
        if root.right:
            rmax = self.maxSum(root.right) # same here
            if rmax > 0: sum += rmax
        if sum > Solution.max: Solution.max = sum
        return max(root.val, max(root.val + lmax, root.val+rmax))

sol = Solution()
a = TreeNode(1)
a.left = TreeNode(2)
a.right = TreeNode(3)
b = sol.maxPathSum(a)
print b