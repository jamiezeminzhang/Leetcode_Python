# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 08:50:06 2016

Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:
Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].

Example 2:
Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].

@author: zeminzhang
"""

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        length = len(intervals)
        if length == 0: return [newInterval]
        
        def merge2(interval, newInterval): # interval.start is smaller
            if newInterval.start <= interval.end:
                if newInterval.end <= interval.end:
                    return [interval]
                else:
                    interval.end = newInterval.end
                    return [interval]
            else:
                return [interval, newInterval]
            
        if length == 1:
            if intervals[0].start <= newInterval.start:
                return merge2(intervals[0], newInterval)
            else:
                return merge2(newInterval,intervals[0])
            
        # find the right position to insert first
        if newInterval.start < intervals[0].start:
            intervals.insert(0,newInterval)
        elif newInterval.start > intervals[-1].start:
            intervals.append(newInterval)
        else:
            for i in range(length-1):              
                if intervals[i].start <= newInterval.start and \
                newInterval.start <= intervals[i+1].start:
                    intervals.insert(i+1, newInterval)
                    break
        # merge
        res = [intervals[0]]
        for i in range(1,len(intervals)):
            new = intervals[i]
            old = res.pop()
            tmp = merge2(old,new)
            if len(tmp) == 1:
                res.append(tmp[0])
            else:
                res += tmp    
        return res
            
sol = Solution()
a = Interval(0,2)
b = Interval(3,5)
c = Interval(6,8)
d = Interval(4,7)
c = sol.insert([a,b,c],d)
for i in c:
    print i.start, i.end