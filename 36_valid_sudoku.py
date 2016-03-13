# -*- coding: utf-8 -*-
"""
Created on Tue Aug 04 13:40:01 2015

LeetCode # 36: Valid Sudoku
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled with 
the character '.'.


A partially filled sudoku which is valid.

Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the 
filled cells need to be validated. 

@author: zzhang
"""

class Solution:  
    # @param board, a 9x9 2D array  
    # @return a boolean  
    def valid(self,x,y,tmp,board):  
        for i in range(9):  
            if board[i][y]==tmp:  
                return False  
        for j in range(9):  
            if board[x][j]==tmp:  
                return False  
        for i in range(3):  
            for j in range(3):  
                if board[(x/3)*3+i][(y/3)*3+j]==tmp:  
                    return False  
        return True  
    def isValidSudoku(self, board):  
        for i in range(9):  
            for j in range(9):  
                if board[i][j]=='.':  
                    continue  
                tmp=board[i][j]  
                board[i][j]='D'  
                if self.valid(i,j,tmp,board)==False:  
                    return False  
                else:  
                    board[i][j]=tmp  
        return True  