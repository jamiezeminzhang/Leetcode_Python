# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 08:30:28 2016

79. Word Search

Total Accepted: 79097 Total Submissions: 337742 Difficulty: Medium

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, 
where "adjacent" cells are those horizontally or vertically neighboring. 
The same letter cell may not be used more than once.

For example,
Given board =

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.

解题思路：使用dfs来搜索，为了避免已经用到的字母被重复搜索，将已经用到的字母临时替换为'#'就可以了

@author: zeminzhang
"""

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m, n = len(board), len(board[0])
        def dfs(x, y, word):
            if len(word)==0: return True
            if board[x][y] != word[0]: return False
            else:
                if len(word) == 1: return True #last letter already match
                tmp = board[x][y]
                board[x][y] = '#'
                for dx, dy in [[-1,0],[1,0],[0,-1],[0,1]]:
                    nx, ny = x+dx, y+dy
                    if nx>=0 and nx<m and ny>=0 and ny<n:
                        if dfs(nx, ny, word[1:]): return True
                board[x][y] = tmp
        
        for i in range(m):
            for j in range(n):
                if dfs(i, j, word): return True
        return False