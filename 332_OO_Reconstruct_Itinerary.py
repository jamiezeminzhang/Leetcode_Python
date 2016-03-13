# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 10:34:58 2016

332. Reconstruct Itinerary My Submissions Question
Total Accepted: 4146 Total Submissions: 18023 Difficulty: Medium
Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

Note:
If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
All airports are represented by three capital letters (IATA code).
You may assume all tickets form at least one valid itinerary.
Example 1:
tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Return ["JFK", "MUC", "LHR", "SFO", "SJC"].
Example 2:
tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Return ["JFK","ATL","JFK","SFO","ATL","SFO"].
Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"]. But it is larger in lexical order.

My solution: TLE
class Solution(object):
    def findItinerary(self, tickets):        
        def dfs(tickets, lis):
            if tickets == []: 
                ans.append(lis)
            for i, ticket in enumerate(tickets):
                if ticket[0] == lis[-1]:
                    dfs(tickets[:i]+tickets[i+1:], lis+[ticket[1]])
        
        ans = []
        for i, ticket in enumerate(tickets):
            if ticket[0] == 'JFK':
                dfs(tickets[:i]+tickets[i+1:],ticket)
        return min(ans)
        
@author: Jamie
"""
import collections
class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        targets = collections.defaultdict(list)
        for a,b in sorted(tickets)[::-1]:
            targets[a] += b,

        route = []
        def dfs(airport):
            while targets[airport]:
                dfs(targets[airport].pop())
            route.append(airport)
        dfs('JFK')
        return route[::-1]

sol = Solution()
print sol.findItinerary([["JFK","SFO"],["SFO","ATL"],["ATL","END"]])