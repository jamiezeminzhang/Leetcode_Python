# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 20:58:22 2016

The n-queens puzzle is the problem of placing n queens on an n×n chessboard 
such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' 
placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

For example,
There exist two distinct solutions to the 4-queens puzzle:

[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]

check函数用来检查在第k行，皇后是否可以放置在第j列。

@author: zeminzhang
"""

class Solution:
    # @return a list of lists of string
    def solveNQueens(self, n):
        
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
        return res
    
        
sol = Solution()
print sol.solveNQueens(4)
    
    
                            