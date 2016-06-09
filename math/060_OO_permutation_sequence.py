# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 23:22:14 2016

60. Permutation Sequence 

The set [1,2,3,…,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note: Given n will be between 1 and 9 inclusive.

@author: zeminzhang
"""
class Solution:
    """
    @param n: n
    @param k: the k-th permutation
    @return: the k-th permutation
    """
    def getPermutation(self, n, k):
        fac = [1]
        for i in range(1, n + 1):
            fac.append(fac[-1] * i)
        
        elegible = range(1, n + 1)
        per = []
        for i in range(n):
            digit = (k - 1) / fac[n - i - 1]
            per.append(elegible[digit])
            elegible.remove(elegible[digit])
            k = (k - 1) % fac[n - i - 1] + 1
        return "".join([str(x) for x in per])
        
a = Solution()
print a.getPermutation(4,2)
