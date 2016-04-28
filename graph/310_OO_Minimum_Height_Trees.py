# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 00:17:19 2016

310. Minimum Height Trees

Total Accepted: 7623 Total Submissions: 29247 Difficulty: Medium

For a undirected graph with tree characteristics, we can choose any node as the root. 
The result graph is then a rooted tree. Among all possible rooted trees, those with minimum 
height are called minimum height trees (MHTs). Given such a graph, write a function to find all 
the MHTs and return a list of their root labels.

Format
The graph contains n nodes which are labeled from 0 to n - 1. You will be given the number n and a 
list of undirected edges (each edge is a pair of labels).

You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] 
is the same as [1, 0] and thus will not appear together in edges.

Example 1:

Given n = 4, edges = [[1, 0], [1, 2], [1, 3]]

        0
        |
        1
       / \
      2   3
return [1]

Example 2:

Given n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]

     0  1  2
      \ | /
        3
        |
        4
        |
        5
return [3, 4]

Hint:

How many MHTs can a graph have at most?   

** Answer: 2 **


Note:

(1) According to the definition of tree on Wikipedia: “a tree is an undirected graph in 
which any two vertices are connected by exactly one path. In other words, any connected graph
 without simple cycles is a tree.”

(2) The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.


** 大致思路**
像剥洋葱一样一层层剥开

对每一个顶点x，将与他相邻的顶点都存起来: children[x] = set(a,b,c,d...)
找到所有只有一个相邻顶点的点。这些点是叶子。
每一次循环将所有的叶子节点删掉，并更新新的叶子节点。直到新的叶子节点的个数不大于2个。
所求则是最后的叶子节点。


@author: Jamie
"""

class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        children = [set() for x in range(n)]
        #children = collections.defaultdict(set)      #或者用这个也行
        for left, right in edges:
            children[left].add(right)
            children[right].add(left)
        leaves = [x for x in range(n) if len(children[x]) <= 1]
        
        while n>2:
            n -= len(leaves)
            new_leaves = []
            for x in leaves:
                for y in children[x]:
                    children[y].remove(x)
                    if len(children[y]) == 1: 
                        new_leaves.append(y)
            leaves = new_leaves
        return leaves