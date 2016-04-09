# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 04:48:03 2016

96. Unique Binary Search Trees My Submissions Question
Total Accepted: 73630 Total Submissions: 200933 Difficulty: Medium
Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

For example,
Given n = 3, there are a total of 5 unique BST's.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

定义f(n)为unique BST的数量，以n = 3为例：

构造的BST的根节点可以取{1, 2, 3}中的任一数字。

如以1为节点，则left subtree只能有0个节点，而right subtree有2, 3两个节点。
所以left/right subtree一共的combination数量为：f(0) * f(2) = 2

以2为节点，则left subtree只能为1，right subtree只能为2：f(1) * f(1) = 1

以3为节点，则left subtree有1, 2两个节点，right subtree有0个节点：f(2)*f(0) = 2

@author: zeminzhang
"""

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1: return 1
        if n == 2: return 2
        dp = [0 for x in range(n+1)]
        dp[0],dp[1],dp[2] = 1,1,2
        for i in range(3,n+1):
            res = 0
            for j in range(i):
                res += (dp[j]*dp[i-1-j])
            dp[i] = res
        
        return dp[n]