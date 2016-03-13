# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 22:19:56 2016

99. Recover Binary Search Tree My Submissions Question
Total Accepted: 46994 Total Submissions: 182612 Difficulty: Hard
Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Note:
A solution using O(n) space is pretty straight forward. Could you devise a 
constant space solution?

############
##############

I only got a O(n) solution.

The constant solution is given here.

算法二：

题目有一个附加要求就是要求空间复杂度为常数空间。而算法一的空间复杂度为O(N)，还不够省空间。
以下的解法也是中序遍历的写法，只是非常巧妙，使用了一个prev指针。例如一颗被破坏的二叉查找树如下：

　　　　　　　  　4

　　　　　　 　/     \
         
           2        6
        
         /   \    /   \
   
        1     5  3      7

很明显3和5颠倒了。那么在中序遍历时：当碰到第一个逆序时：为5->4，那么将n1指向5，n2指向4，
注意，此时n1已经确定下来了。然后prev和root一直向后遍历，直到碰到第二个逆序时：4->3，
此时将n2指向3，那么n1和n2都已经确定，只需要交换节点的值即可。prev指针用来比较中序遍历中相邻两个值的大小关系，很巧妙。 

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a tree node
    def FindTwoNodes(self, root):
            if root:
                self.FindTwoNodes(root.left)
                if self.prev and self.prev.val > root.val:
                    self.n2 = root
                    if self.n1 == None: self.n1 = self.prev
                self.prev = root
                self.FindTwoNodes(root.right)
    def recoverTree(self, root):
        self.n1 = self.n2 = None
        self.prev = None
        self.FindTwoNodes(root)
        self.n1.val, self.n2.val = self.n2.val, self.n1.val
        return root
        
@author: zeminzhang
"""

#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root: return root
        def dfs(root):
            if root:
                dfs(root.left)
                res.append(root.val)
                resp.append(root)
                dfs(root.right)
        res,resp = [], []
        dfs(root)
        idx1,idx2 = -1, -1
        if len(res) == 2:
            idx1, idx2 = 0,1
        else:
            for i in range(len(res)-1):
                if res[i] > res[i+1] :
                    idx1 = i
                    for j in range(i+1, len(res)-1):
                        if res[i] >= res[j-1] and res[i] < res[j+1]:
                            idx2 = j
                            break
                    break
        resp[idx1].val = res[idx2]
        resp[idx2].val = res[idx1]
                    
           
                    
           