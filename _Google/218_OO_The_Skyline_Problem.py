# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 08:10:36 2016

218. The Skyline Problem

Total Accepted: 16006 Total Submissions: 73218 Difficulty: Hard

A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. 
Now suppose you are given the locations and height of all the buildings as shown on a cityscape photo (Figure A), 
write a program to output the skyline formed by these buildings collectively (Figure B).


Buildings  Skyline Contour
The geometric information of each building is represented by a triplet of integers [Li, Ri, Hi], where Li and Ri are the x 
coordinates of the left and right edge of the ith building, respectively, and Hi is its height. 
It is guaranteed that 0 ≤ Li, Ri ≤ INT_MAX, 0 < Hi ≤ INT_MAX, and Ri - Li > 0. You may assume all buildings are perfect 
rectangles grounded on an absolutely flat surface at height 0.

For instance, the dimensions of all buildings in Figure A are recorded as: [ [2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8] ] .
The output is a list of "key points" (red dots in Figure B) in the format of [ [x1,y1], [x2, y2], [x3, y3], ... ] that uniquely 
defines a skyline. A key point is the left endpoint of a horizontal line segment. Note that the last key point, where the 
rightmost building ends, is merely used to mark the termination of the skyline, and always has zero height. Also, the ground 
in between any two adjacent buildings should be considered part of the skyline contour.

For instance, the skyline in Figure B should be represented as:[ [2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0] ].

Notes:

1. The number of buildings in any input list is guaranteed to be in the range [0, 10000].
2. The input list is already sorted in ascending order by the left x position Li.
3. The output list must be sorted by the x position.
4. There must be no consecutive horizontal lines of equal height in the output skyline. For instance, [...[2 3], [4 5], [7 5], [11 5], [12 7]...] is not acceptable; the three lines of height 5 should be merged into one in the final output as such: [...[2 3], [4 5], [12 7], ...]


************

Use an infinite vertical line x to scan from left to right. If max height changes, record [x, height] 
in res. Online judge is using Python 2.7.9 and there's no max heap's push and pop method, 
so we can use a min heap hp storing -H as "max heap".

*** 
    用的最大堆heap
    heap里存的是 【负楼高，楼右侧坐标】
    heap 顶端是*＊当前＊＊最高的楼
    每次循环，如果 来的坐标 x 大于等于 heap顶端元素（目前最高楼）楼右侧坐标，那么堆顶元素出栈。堆最高楼更新。
    event中第二部分加上的意义在于写出所有的楼的右边的轮廓。考虑只有一个楼的情况就清楚了。
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
            if res[-1][1] + hp[0][0]:  # 记住是和栈顶元素比较
                res += [x, -hp[0][0]],
        return res[1:]

sol = Solution()
print sol.getSkyline([ [2,9,10], [3 ,7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8] ])
