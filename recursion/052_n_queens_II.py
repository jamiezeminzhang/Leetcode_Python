# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 02:33:52 2016

52. N-Queens II

Total Accepted: 45230 Total Submissions: 113751 Difficulty: Hard

Follow up for N-Queens problem.

Now, instead outputting board configurations, return the total number of distinct solutions.

@author: zeminzhang
"""

class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        def check(k, j):  # check if the kth queen can be put in column j!
            for i in range(k):
                if board[i]==j or abs(k-i)==abs(board[i]-j): #这个对角好精髓
                    return False
            return True
            
        def dfs(depth, valuelist):
            if depth==n: res.append(valuelist); return
            for i in range(n):
                if check(depth,i): 
                    board[depth]=i
                    s='.'*n
                    dfs(depth+1, valuelist+[s[:i]+'Q'+s[i+1:]])
        board=[-1 for i in range(n)] # board[i] = j 意味着第i行的queen在j列上
        res=[]
        dfs(0,[])
        return len(res)