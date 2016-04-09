# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 17:17:14 2016

216. Combination Sum III My Submissions Question

Total Accepted: 25029 Total Submissions: 73066 Difficulty: Medium
Find all possible combinations of k numbers that add up to a number n, given that only numbers 
from 1 to 9 can be used and each combination should be a unique set of numbers.

Ensure that numbers within the set are sorted in ascending order.


Example 1:

Input: k = 3, n = 7

Output:

[[1,2,4]]

Example 2:

Input: k = 3, n = 9

Output:

[[1,2,6], [1,3,5], [2,3,4]]

用start来控制顺序， 并且保证不重复。 太简洁漂亮了。

@author: Jamie
"""

class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        
        def dfs(start, count, sums, num_list):
            if count >k or sums>n:
                return
            if count == k and sums == n:
                res.append(num_list)
                return
            for x in range(start+1,10):
                dfs(x, count+1, sums+x, num_list + [x])
                
        res = []
        dfs(0,0,0,[])
        return res
        
sol = Solution()
#print sol.combinationSum3(6,30)
print sol.combinationSum3(9,45)