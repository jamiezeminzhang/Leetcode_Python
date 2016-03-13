# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 01:50:21 2016

130. Surrounded Regions My Submissions Question

Total Accepted: 47035 Total Submissions: 299943 Difficulty: Medium
Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

For example,
X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X

## My solution:
Line 29: RuntimeError: maximum recursion depth exceeded in cmp
dfs代码，因为递归深度的问题会爆栈

class Solution(object):
    def solve(self, board):
        length1 = len(board)
        if length1 == 0: return
        length2 = len(board[0])
        if length2 == 0: return
        visit = [[False for x in range(length2)] for y in range(length1)]
        for i in range(length1):
            if board[i][0] == '0' and not visit[i][0]:
                self.dfs(board,visit,i,0)
            if board[i][length2-1] == '0' and not visit[i][length2-1]:
                self.dfs(board,visit,i,length2-1)
        for j in range(length2):
            if board[0][j] == '0' and not visit[0][j]:
                self.dfs(board,visit,0,j)
            if board[length1-1][j] == '0' and not visit[length1-1][j]:
                self.dfs(board,visit,length1-1,j)
        for i in range(length1):
            for j in range(length2):
                if not visit[i][j]:
                    board[i][j] = 'X'
                    
    def dfs(self, board, visit, idx1, idx2):
        length1, length2 = len(board), len(board[0])
        if board[idx1][idx2] == 'X': return
        else:
            if visit[idx1][idx2]: return
            else:
                visit[idx1][idx2] = True
                if idx1-1 >=0 and idx1-1 <= length1-1: # up
                    self.dfs(board,visit,idx1-1,idx2)
                if idx1+1 >=0 and idx1+1 <= length1-1: # down
                    self.dfs(board,visit,idx1+1,idx2)
                if idx2+1 >=0 and idx2+1 <= length2-1: # right
                    self.dfs(board,visit,idx1,idx2+1)
                if idx2-1 >=0 and idx2-1 <= length2-1: # left
                    self.dfs(board,visit,idx1,idx2-1)
@author: zeminzhang

*** 解题思路：这道题可以使用BFS和DFS两种方法来解决。DFS会超时。BFS可以AC。从边上开始搜索，
如果是'O'，那么搜索'O'周围的元素，并将'O'置换为'D'，这样每条边都DFS或者BFS一遍。
而内部的'O'是不会改变的。这样下来，没有被围住的'O'全都被置换成了'D'，被围住的'O'还是'O'，
没有改变。然后遍历一遍，将'O'置换为'X'，将'D'置换为'O'。

"""

class Solution:
    # @param board, a 9x9 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    def solve(self, board):
        def fill(x, y):
            if x<0 or x>m-1 or y<0 or y>n-1 or board[x][y] != 'O': return
            queue.append((x,y))
            board[x][y]='D'
        def bfs(x, y):
            if board[x][y]=='O':queue.append((x,y)); fill(x,y)
            while queue:
                curr=queue.pop(0); i=curr[0]; j=curr[1]
                fill(i+1,j);fill(i-1,j);fill(i,j+1);fill(i,j-1)
        if len(board)==0: return
        m=len(board); n=len(board[0]); queue=[]
        for i in range(n):
            bfs(0,i); bfs(m-1,i)
        for j in range(1, m-1):
            bfs(j,0); bfs(j,n-1)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'D': board[i][j] = 'O'
                elif board[i][j] == 'O': board[i][j] = 'X'

class my_Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def fill(x, y):
            if x<0 or x>m-1 or y<0 or y > n-1 or board[x][y] != 'O': return
            queue.append((x,y))
            board[x][y] = 'D'
        
        def bfs(x,y):
            if board[x][y] == 'O': fill(x,y)
            while queue:
                curr = queue.pop(0); curr1,curr2 = curr[0],curr[1]
                fill(curr1+1,curr2);fill(curr1-1,curr2);fill(curr1,curr2+1);fill(curr1,curr2-1)
        
        if len(board) ==0: return 
        m,n = len(board), len(board[0]);queue = []
        for i in range(m):
            bfs(i,0);bfs(i,n-1)
        for j in range(n):
            bfs(0,j);bfs(m-1,j)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'D': board[i][j] = 'O'
                elif board[i][j] == 'O': board[i][j] = 'X'

sol = Solution()
#board = [ ['X','X','X'] ,['X','0','X'],['X','X','X']]
board = [ ['O'] ]
sol.solve(board)
print board