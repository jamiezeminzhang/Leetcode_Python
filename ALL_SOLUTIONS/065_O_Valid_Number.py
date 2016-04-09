# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 02:12:41 2016

Validate if a given string is numeric.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
Note: It is intended for the problem statement to be ambiguous. 
You should gather all requirements up front before implementing one.

@author: zeminzhang
"""

class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        num = {'0','1','2','3','4','5','6','7','8','9','0'}
        sign = {'.','e',' '}
        
        i1, i2 = 0, len(s)-1
        while s[i1] == ' ':
            if i1 == len(s)-1: return False
            else:
                i1 +=1
        while s[i2] == ' ':
            if i2 == 0 : return False
            else:
                i2 -=1
        
        if i1>i2: return False
        s = s[i1:i2+1]
        if s[0] == '+' or s[0] == '-':
            s = s[1:]
        
        length = len(s)
        for idx, i in enumerate(s):
#            print i
            # other characters
            if i not in num and i not in sign:
                if i == '+' or i == '-':
                    if s[idx-1] != 'e':
                        return False
                else:
                    return False
            # if period
            # string before it should be pure math
            # string after it may contain e
            if i == '.':
                # string before it
                idx2 = 0
                if idx != 0:
                    for j in s[idx2:idx]:
                        if j not in num:
                            return False
                        
                # string after it
                if idx == length-1 and idx == 0: return False
                if idx != length-1 and idx ==0 and s[idx+1] == 'e': return False
                flag_e = 0 # flag for # of e's
                idx3 = length - 1
                for j in range(idx+1,idx3+1):
                    if s[j] == ' ' or s[j] == '.': return False
                    if s[j] == 'e':
                        if flag_e == 0: 
                            flag_e =1
                        else:
                            return False
            if i == ' ': return False
            if i == 'e':
                if idx == length-1 : return False
                elif idx == 0: return False
                else:
                    flag_p = 0
                    for ss in s[:idx]:
                        if ss not in num and ss != '.': return False
                        if ss == '.':
                            if flag_p == 0: flag_p == 1
                            else:
                                return False
                    if s[idx+1] == '+' or s[idx+1] == '-':
                        if idx+1 == length -1: return False
                        else:
                            for sss in s[idx+2:]:
                                if sss not in num: return False
                    else:
                        for sss in s[idx+1:]:
                            if sss not in num: 
                                return False
                    
        return True
                    
sol = Solution()
print sol.isNumber("4e+")
        