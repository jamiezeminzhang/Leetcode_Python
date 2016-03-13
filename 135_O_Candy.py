# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 07:25:30 2016

135. Candy My Submissions Question

Total Accepted: 47521 Total Submissions: 217705 Difficulty: Hard
There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?

@author: zeminzhang
"""

class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        length = len(ratings)
        if length == 0: return 0
        if length == 1: return 1
        candy = [1 for x in range(length)]
        for i in range(length-1):
            if ratings[i] < ratings[i+1]:
                candy[i+1] = candy[i] + 1
        for i in range(length-1,0,-1):
            if ratings[i] < ratings[i-1] and candy[i] >= candy[i-1]: # important second condition 
                candy[i-1] = candy[i] + 1
        return sum(candy)
        
sol = Solution()
print sol.candy([4,2,3,4,1])
#print sol.candy([1,3,4,3,2,1])
        