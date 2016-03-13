# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 03:19:50 2016

134. Gas Station My Submissions Question

Total Accepted: 55556 Total Submissions: 207242 Difficulty: Medium
There are N gas stations along a circular route, where the amount of gas at 
station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel 
from station i to its next station (i+1). You begin the journey with an empty 
tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit 
once, otherwise return -1.

Note:
The solution is guaranteed to be unique.


解题思路：这道题也很tricky，自己想是很难想出来的。如果sum(gas)<sum(cost)的话，那么一定无解。
diff是走完一站邮箱剩下的油，如果加上gas[i]也到不了下一站，那么继续将下一站设置为起点，然后再检查，是不是很巧妙呢？
@author: zeminzhang
"""
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        length = len(gas)
        if length == 0: return -1
        if length == 1: return 0 if gas[0]>=cost[0] else -1
        if sum(gas) < sum(cost): return -1
        i = 0
        while i< length:
            gas_tmp = gas[i:]+gas[:i]
            cost_tmp = cost[i:]+cost[:i]
            diff = 0
            for j in range(length):
                diff += (gas_tmp[j] - cost_tmp[j])
                if diff<0:        
                    i = (i+j+1)
                    break
            if j == length-1: return i
        return -1

sol = Solution()
print sol.canCompleteCircuit([1,2],[2,1])