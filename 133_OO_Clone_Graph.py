# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 10:39:32 2016

133. Clone Graph My Submissions Question
Total Accepted: 58728 Total Submissions: 238122 Difficulty: Medium
Clone an undirected graph. Each node in the graph contains a label and a list 
of its neighbors.


OJ's undirected graph serialization:
Nodes are labeled uniquely.

We use # as a separator for each node, and , as a separator for node label and 
each neighbor of the node.
As an example, consider the serialized graph {0,1,2#1,2#2,2}.

The graph has a total of three nodes, and therefore contains three parts as 
separated by #.

First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
Second node is labeled as 1. Connect node 1 to node 2.
Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming 
a self-cycle.
Visually, the graph looks like the following:

       1
      / \
     /   \
    0 --- 2
         / \
         \_/

@author: zeminzhang
** Given is dfs
here is the bfs code

class Solution(object):
    def cloneGraph(self, node):
        if node == None: return None
        queue = []; dic = {}
        head = UndirectedGraphNode(node.label)
        queue.append(node)
        dic[node] = head
        
        while queue:
            cur = queue.pop(0)
            for neighbor in cur.neighbors:
                if neighbor not in dic:
                    tmp = UndirectedGraphNode(neighbor.label)
                    dic[cur].neighbors.append(tmp)
                    dic[neighbor] = tmp
                    queue.append(neighbor)
                else:
                    dic[cur].neighbors.append(dic[neighbor])
        return head
        
"""

# Definition for a undirected graph node
class UndirectedGraphNode(object):
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode
        """
        def dfs(node, dic):
            if node in dic: return dic[node]
            else:
                tmp = UndirectedGraphNode(node.label)
                dic[node] = tmp
                for i in node.neighbors:
                    tmp.neighbors.append(dfs(i,dic))
            return tmp
        if node == None: return None
        return dfs(node, {})
        