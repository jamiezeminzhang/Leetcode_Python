# -*- coding: utf-8 -*-
"""
Created on Thursday Sep 1 9:12:20 2016

286. Walls and Gates  

Total Accepted: 13854
Total Submissions: 35401
Difficulty: Medium

You are given a m x n 2D grid initialized with these three possible values.

-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

For example, given the 2D grid:
INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF
After running your function, the 2D grid should be:
  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4

@author: Jamie
"""

class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        if not rooms: return
        m, n = len(rooms), len(rooms[0])
        queue = collections.deque()
        for i in range(m):
            for j in range(n):
                if rooms[i][j]==0:
                    queue.append((i, j, 0))
        
        while queue:
            x ,y, num = queue.popleft()
            for dx, dy in zip([0,1,0,-1],[1,0,-1,0]):
                nx, ny = x+dx, y+dy
                if nx>=0 and nx<m and ny>=0 and ny<n and rooms[nx][ny]==2147483647:
                    rooms[nx][ny] = num+1
                    queue.append((nx,ny,num+1))
        