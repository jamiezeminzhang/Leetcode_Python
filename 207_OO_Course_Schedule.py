# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 16:30:44 2016

207. Course Schedule My Submissions Question

Total Accepted: 31793 Total Submissions: 122872 Difficulty: Medium
There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to 
first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it 
possible for you to finish all courses?

For example:

2, [[1,0]]
There are a total of 2 courses to take. To take course 1 you should have 
finished course 0. So it is possible.

2, [[1,0],[0,1]]
There are a total of 2 courses to take. To take course 1 you should have 
finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

Note:
The input prerequisites is a graph represented by a list of edges, not 
adjacency matrices. Read more about how a graph is represented.

click to show more hints.

Hints:

This problem is equivalent to finding if a cycle exists in a directed graph. 
If a cycle exists, no topological ordering exists and therefore it will be 
impossible to take all courses.
Topological Sort via DFS - A great video tutorial (21 minutes) on Coursera 
explaining the basic concepts of Topological Sort.
Topological sort could also be done via BFS.

http://www.cnblogs.com/grandyang/p/4484571.html

第二条提示是在讲如何来表示一个有向图，可以用边来表示，边是由两个端点组成的，用两个点来表示边。
第三第四条提示揭示了此题有两种解法，DFS和BFS都可以解此题。我们先来看BFS的解法，
我们定义二维数组graph来表示这个有向图，一位数组in来表示每个顶点的入度。
我们开始先根据输入来建立这个有向图，并将入度数组也初始化好。然后我们定义一个queue变量，
将所有入度为0的点放入队列中，然后开始遍历队列，从graph里遍历其连接的点，每到达一个新节点，
将其入度减一，如果此时该点入度为0，则放入队列末尾。直到遍历完队列中所有的值，
若此时还有节点的入度不为0，则说明环存在，返回false，反之则返回true。代码为AC代码。

DFS的代码在这里

下面我们来看DFS的解法，也需要建立有向图，还是用二维数组来建立，和BFS不同的是，
我们像现在需要一个一维数组visit来记录访问状态，大体思路是，先建立好有向图，
然后从第一个门课开始，找其可构成哪门课，暂时将当前课程标记为已访问，
然后对新得到的课程调用DFS递归，直到出现新的课程已经访问过了，则返回false，
没有冲突的话返回true，然后把标记为已访问的课程改为未访问。代码如下：

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        graph = {}; visit= {}
        for pair in prerequisites:
            graph[pair[1]] = graph.get(pair[1],[]) + [pair[0]]
            graph[pair[0]] = graph.get(pair[0],[])
            visit[pair[0]] = visit.get(pair[0],0)
            visit[pair[1]] = visit.get(pair[1],0)
        vertices = visit.keys()
        
        # -1 means visited; 1 means not visited
        def canFinishDFS(vertice):
            if visit[vertice] == -1: return False
            if visit[vertice] == 1 : return True
            visit[vertice] = -1
            
            for v in graph[vertice]:
                if not canFinishDFS(v): return False
            visit[vertice] = 1
            return True
            
        for v in vertices:
            if not canFinishDFS(v): return False
        return True
        

@author: zzhang04
"""

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        InDegree = {}
        for pair in prerequisites:
            InDegree[pair[0]] = InDegree.get(pair[0],0)
            InDegree[pair[1]] = InDegree.get(pair[1],0)
        for pair in prerequisites:
            InDegree[pair[0]] += 1
        
        queue = []
        for vertice in InDegree:
            if InDegree[vertice] == 0: queue.append(vertice)
        
        while queue:
            vertice = queue.pop()
            for pair in prerequisites:
                if vertice == pair[1]:
                    InDegree[pair[0]] -= 1
                    if InDegree[pair[0]] == 0: queue.insert(0,pair[0])
        print InDegree
        for i in InDegree:
            if InDegree[i] != 0: return False
        return True