# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 21:33:28 2016

Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].

解题思路：先将区间按照每个start的值来排序，排好序以后判断一个区间的start值是否处在前
一个区间中，如果在前一个区间中，那么合并；如果不在，就将新区间添加。

@author: zeminzhang
"""

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        length = len(intervals)
        if length == 0: return []
        if length == 1: return intervals
            
        intervals.sort(key = lambda x:x.start)
        
        res = [intervals[0]]
        for i in range(1,length):
            new = intervals[i]
            old = res.pop()
            if new.start >= old.start and new.start <= old.end:
                if new.end > old.end :
                    res.append(Interval(old.start, new.end))
                else:
                    res.append(old)
            if new.start > old.end:
                res.append(old)
                res.append(new)
        
        return res
                
sol = Solution()
a = Interval(1,4)
b = Interval(5,6)
c = Interval(3,3)
d = Interval(1,3)
c = sol.merge([a,b])
for i in c:
    print i.start, i.end
                    
        

                
            