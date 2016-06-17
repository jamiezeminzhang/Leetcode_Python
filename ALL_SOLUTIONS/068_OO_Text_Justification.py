# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 04:28:53 2016

68. Text Justification

Total Accepted: 34873 Total Submissions: 212254 Difficulty: Hard

Given an array of words and a length L, format the text such that each line has
 exactly L characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as 
you can in each line. Pad extra spaces ' ' when necessary so that each line has 
exactly L characters.

Extra spaces between words should be distributed as evenly as possible. If the
 number of spaces on a line do not divide evenly between words, the empty slots 
 on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is 
inserted between words.

For example,
words: ["This", "is", "an", "example", "of", "text", "justification."]
L: 16.

Return the formatted lines as:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]

*** A better solution ***
直接法：
1.每次向cur里面放word，并且更新总词长num_of_letters。 直到总长度>maxWidth。然后判断cur中词的个数。
2.如果只有一个词，那么靠左，右边加上适当空格
3.如果有多个词，那么用divmod算出词距。多的词距加到cur[i]的结尾。
如果总长度大于>maxWidth，以上两步结束之后，重置cur和num_of_letters。
***
def fullJustify(self, words, maxWidth):
    res, cur, num_of_letters = [], [], 0
    for w in words:
        if num_of_letters + len(w) + len(cur) > maxWidth:
            if len(cur) == 1:
                res.append( cur[0] + ' '*(maxWidth - num_of_letters) )
            else:
                num_spaces = maxWidth - num_of_letters - len(cur) + 1
                space_between_words, num_extra_spaces = divmod( num_spaces, len(cur)-1)
                for i in range(num_extra_spaces):
                    cur[i] += ' '
                res.append( (' '*(1+space_between_words)).join(cur) )
            cur, num_of_letters = [], 0
        cur += [w]
        num_of_letters += len(w)
    res.append( ' '.join(cur) + ' '*(maxWidth - num_of_letters - len(cur) + 1) )
    return res
	
@author: zeminzhang
"""

class Solution:
    # @param words, a list of strings
    # @param L, an integer
    # @return a list of strings
    def fullJustify(self, words, L):
        res=[]
        i=0
        while i<len(words):
            size=0; begin=i
            while i<len(words):
                newsize=len(words[i]) if size==0 else size+len(words[i])+1
                if newsize<=L: size=newsize
                else: break
                i+=1
            spaceCount=L-size
            if i-begin-1>0 and i<len(words):
                everyCount=spaceCount/(i-begin-1)
                spaceCount%=i-begin-1
            else:
                everyCount=0
            j=begin
            while j<i:
                if j==begin: s=words[j]
                else:
                    s+=' '*(everyCount+1)
                    if spaceCount>0 and i<len(words):
                        s+=' '
                        spaceCount-=1
                    s+=words[j]
                j+=1
            s+=' '*spaceCount
            res.append(s)
        return res
            
        
            
            
            
words = ["This", "is", "an", "example", "of", "text", "justification."]
L = 16
sol = Solution()
print sol.fullJustify(words,L)
            
            
            
            