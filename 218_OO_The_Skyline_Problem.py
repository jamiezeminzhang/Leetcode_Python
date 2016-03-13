# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 08:10:36 2016

votes
180 views
Use an infinite vertical line x to scan from left to right. If max height changes, record [x, height] 
in res. Online judge is using Python 2.7.9 and there's no max heap's push and pop method, 
so we can use a min heap hp storing -H as "max heap".


def getSkyline(self, buildings):
    events = sorted([(L, -H, R) for L, R, H in buildings] + list(set((R, 0, None) for L, R, H in buildings)))
    res, hp = [[0, 0]], [(0, float("inf"))]
    for x, negH, R in events:
        while x >= hp[0][1]: 
            heapq.heappop(hp)
        if negH: heapq.heappush(hp, (negH, R))
        if res[-1][1] + hp[0][0]: 
            res += [x, -hp[0][0]],
    return res[1:]

*** heap里存的是 【楼高，楼右侧坐标】
    heap 顶端是到现在最高的楼
    每次循环，如果 来的坐标 x 大于等于 heap顶端元素（目前最高楼）楼右侧坐标，那么堆顶元素出栈。堆最高楼更新。
    对于每个新来的 x ，如果当前堆顶元素的楼高和res中最后一个楼高不同，意味着堆最高楼高更新了，新的pair加入res
    
@author: Jamie
"""
import heapq
class Solution(object):
    def getSkyline(self, buildings):
        #events = sorted([(L, -H, R) for L, R, H in buildings] + list(set((R, 0, None) for L, R, H in buildings)))
        events = sorted([(L, -H, R) for L, R, H in buildings] + list({(R, 0, None) for _, R, _ in buildings}))
        res, hp = [[0, 0]], [(0, float("inf"))]
        for x, negH, R in events:
            while x >= hp[0][1]: 
                heapq.heappop(hp)
            if negH: 
                heapq.heappush(hp, (negH, R))
            if res[-1][1] + hp[0][0]: 
                res += [x, -hp[0][0]],
        return res[1:]

sol = Solution()
print sol.getSkyline([ [2,9,10], [3 ,7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8] ])