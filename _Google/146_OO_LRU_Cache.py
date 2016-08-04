# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 11:20:09 2016

146. LRU Cache 

Total Accepted: 62503 Total Submissions: 399108 Difficulty: Hard

Design and implement a data structure for Least Recently Used (LRU) cache. 
It should support the following operations: get and set.

get(key) - Get the value (will always be positive) of the key if the key exists
 in the cache, otherwise return -1.
set(key, value) - Set or insert the value if the key is not already present. 
When the cache reached its capacity, it should invalidate the least recently 
used item before inserting a new item.

Cache简介：

Cache(高速缓存)， 一个在计算机中几乎随时接触的概念。CPU中Cache能极大提高存取数据和指令的时间，
让整个存储器(Cache+内存)既有Cache的高速度，又能有内存的大容量；操作系统中的内存page中使用的
Cache能使得频繁读取的内存磁盘文件较少的被置换出内存，从而提高访问速度；数据库中数据查询也用到
Cache来提高效率；即便是Powerbuilder的DataWindow数据处理也用到了Cache的类似设计。
Cache的算法设计常见的有FIFO(first in first out)和LRU(least recently used)。
根据题目的要求，显然是要设计一个LRU的Cache。

解题思路：

Cache中的存储空间往往是有限的，当Cache中的存储块被用完，而需要把新的数据Load进Cache的时候，
我们就需要设计一种良好的算法来完成数据块的替换。LRU的思想是基于“最近用到的数据被重用的概率比较
早用到的大的多”这个设计规则来实现的。

collections.OrderedDict : dictionary with orders

@author: zeminzhang
"""

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.length = 0
        self.dict = collections.OrderedDict()

    def get(self, key):
        """
        :rtype: int
        """
        if key in self.dict:
            val = self.dict[key]
            del self.dict[key]
            self.dict[key] = val
            return val
        else:
            return -1
        

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key in self.dict:
            del self.dict[key]
            self.dict[key] = value
        else:
            if self.length == self.capacity:
                self.dict.popitem(last=False)
                self.length -= 1
            self.dict[key] = value
            self.length += 1
        
        
