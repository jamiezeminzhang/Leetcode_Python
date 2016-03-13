# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 16:11:32 2016

287. Find the Duplicate Number My Submissions Question

Total Accepted: 20653 Total Submissions: 54516 Difficulty: Hard
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), 
prove that at least one duplicate number must exist. Assume that there is only one duplicate number, 
find the duplicate one.

Note:
You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.

解法I： 很难 O(n)
解决本题需要的主要技巧就是要注意到：由于数组的n + 1个元素范围从1到n，我们可以将数组考虑成一个从集合{1, 2, ..., n}到其本身的函数f。这个函数的定义为f(i) = A[i]。基于这个设定，重复元素对应于一对下标i != j满足 f(i) = f(j)。我们的任务就变成了寻找一对(i, j)。一旦我们找到这个值对，只需通过f(i) = A[i]即可获得重复元素。

但是我们怎样寻找这个重复值呢？这变成了计算机科学界一个广为人知的“环检测”问题。问题的一般形式如下：给定一个函数f，序列x_i的定义为

    x_0     = k       (for some k)
    x_1     = f(x_0)
    x_2     = f(f(x_0))
    ...
    x_{n+1} = f(x_n)

假设函数f从定义域映射到它本身，此时会有3种情况。首先，如果定义域是无穷的，则序列是无限长并且没有循环的。例如，函数 f(n) = n + 1，在整数范围内满足这个性质 - 没有数字是重复的。 第二， 序列可能是一个闭合循环，这意味着存在一个i使得x_0 = x_i。在这个例子中，序列在一组值内无限循环。第三，序列有可能是的“ρ型的”，此时序列看起来像下面这样：

      x_0 -> x_1 -> ... x_k -> x_{k+1} ... -> x_{k+j}
                         ^                       |
                         |                       |
                         +-----------------------+

也就是说，序列从一列链条型的元素开始进入一个环，然后无限循环。我们将环的起点称为环的“入口”。

然后和143题一样
Codes below

class Solution(object):
    def findDuplicate(self, nums):
        slow, fast = 0, 0
        
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast: break
        
        finder = 0
        while True:
            slow = nums[slow]
            finder = nums[finder]
            
            if slow == finder: return slow
            

解法II：时间复杂度O(n * log n)

二分查找（Binary Search）+ 鸽笼原理（Pigeonhole Principle）

参考维基百科关于鸽笼原理的词条链接：https://en.wikipedia.org/wiki/Pigeonhole_principle

“不允许修改数组” 与 “常数空间复杂度”这两个限制条件意味着：禁止排序，并且不能使用Map等数据结构

小于O(n2)的运行时间复杂度可以联想到使用二分将其中的一个n化简为log n

参考LeetCode Discuss：https://leetcode.com/discuss/60830/python-solution-explanation-without-changing-input-array

二分枚举答案范围，使用鸽笼原理进行检验

根据鸽笼原理，给定n + 1个范围[1, n]的整数，其中一定存在数字出现至少两次。

假设枚举的数字为 n / 2：

遍历数组，若数组中不大于n / 2的数字个数超过n / 2，则可以确定[1, n /2]范围内一定有解，

否则可以确定解落在(n / 2, n]范围内。

Python代码：

@author: Jamie
"""

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        n = length-1
        
        left, right = 1, n
        while left<=right:
            print (left,right)
            mid = (left + right)/2
            count = sum(x<=mid for x in nums)
            if count<=mid: left = mid+1
            else: right = mid-1
        return left