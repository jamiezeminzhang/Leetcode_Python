# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 09:28:47 2016


Some good solutions:

return n>0 and (bin(n).count('1') == 1)

return n>0 and n&(n-1) == 0 
And of nearby numbers will only be 0 when is like 10000 and 1111 

@author: Jamie
"""

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<=0: return False
        for i in range(64):
            if 2**i == n: return True
        return False