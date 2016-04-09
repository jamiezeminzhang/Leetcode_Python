# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 08:17:53 2016

137. Single Number II My Submissions Question
Total Accepted: 74376 Total Submissions: 202363 Difficulty: Medium


Given an array of integers, every element appears three times except for one. Find that single one.

要求：和single number一样，线性时间复杂度，不能使用额外空间。

解题思路：这道题就比较难了。也是考察位操作。网上的位操作解法看了好半天也没有得其精髓。
由于序列中除了那唯一的一个数之外所有的数都是三个三个出现的。如果把这些数都转换成二进制，
那么二进制数中1的那些位会连续出现三次，我们可以利用这个思路来解题。
比如：3331222转换成二进制为：11 11 11 01 10 10 10。在第1位上，1出现了4次。第2位上，
1出现了6次。那么我们把每一位上为1的个数mod 3剩下的1就是我们所求的数，
比如这个例子：4 mod 3 = 1; 6 mod 3 = 0。这样剩下的二进制位为：01。那最后所求的数就是1了。

那怎么实现这个想法呢？使用二进制模拟三进制。在连续来3个1后清0。使用两个bit位，bit1和bit2。
初始状态bit1和bit2都是0，即00，在来了第一个1后，变成了01，来了第二个1后变成了10，
来了第三个1后，变成了11，然后清0为00，即：00->01->10->11，然后将11清为00，
这个过程就是我们编程的思路。比如如果输入序列为：1 1 1 1 1 1 1，
则变化过程为：00->01->10->11->00->01->10->11->00->01，最后剩下的是1，也就得到了结果。
如果位数多那么以此类推，比如序列为：3 3 3 2 2 2 1。则二进制为：11 11 11 10 10 10 01。
则低位为1 1 1 0 0 0 1，变化过程为：00->01->10->11->00->00->00->00->01，所以低位剩下1。
高位为：1 1 1 1 1 1 0，变化过程为：00->01->10->11->00->01->10->11->00->00，所以高位剩下0。
那么最后剩下的是01，也就是1。如果位数更多，可以以此类推。程序中的one相当于bit1，two相当于bit2。
       
@author: zeminzhang
"""


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        one, two, three = 0,0,0
        for i in range(len(nums)):
            
            two |= nums[i] & one #two为1时，不管A[i]为什么，two都为1
            one = nums[i] ^ one  #异或操作，都是1就进位
            three = ~(one & two) #以下三步的意思是：如果one和two都为1时，就清0，反之则保持原来状态。
            one &= three
            two &= three
#            print one
#            print two
            
        return one

sol = Solution()
print sol.singleNumber([100,100,200,200,400,300,300,100,200,300])