# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 16:23:01 2016

289. Game of Life

Total Accepted: 13145 Total Submissions: 39235 Difficulty: Medium

According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular 
automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell 
interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules 
(taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state.

Follow up: 
Could you solve it in-place? Remember that the board needs to be updated at the same time: You 
cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, 
which would cause problems when the active area encroaches the border of the array. How would you 
address these problems?

@author: Jamie
"""

class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        # 2 stands for dead -> live
        # 3 stands for live -> dead
        # use %2 to make (0,2) the same, (1,3) the same
        
        m, n = len(board), len(board[0])
        
        def update(i, j):
            count = 0
            if i-1>=0 and j-1>=0:     count += board[i-1][j-1]%2
            if i-1>=0:                count += board[i-1][j]  %2
            if i-1>=0 and j+1<=n-1:   count += board[i-1][j+1]%2
            if j-1>=0:                count += board[i][j-1]  %2
            if j+1<=n-1:              count += board[i][j+1]  %2
            if i+1<=m-1 and j-1>=0:   count += board[i+1][j-1]%2
            if i+1<=m-1:              count += board[i+1][j]  %2
            if i+1<=m-1 and j+1<=n-1: count += board[i+1][j+1]%2
            
            if count<2 and board[i][j]==1: board[i][j]=3
            if count>3 and board[i][j]==1: board[i][j]=3
            if count==3 and board[i][j]==0:board[i][j]=2
            
        for i in range(m):
            for j in range(n):
                update(i,j)
        for i in range(m):
            for j in range(n):
                if board[i][j]==2: board[i][j]=1
                if board[i][j]==3: board[i][j]=0