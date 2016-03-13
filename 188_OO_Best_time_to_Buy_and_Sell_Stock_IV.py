# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 03:48:47 2016

188. Best Time to Buy and Sell Stock IV My Submissions Question

Total Accepted: 21316 Total Submissions: 100576 Difficulty: Hard
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock 
before you buy again).

Credits:
Special thanks to @Freezen for adding this problem and creating all test cases.

很自然的，做决策求最值，会想到用 DP （动态规划）来完成这道题。

 

再来思考问题的本质，可以发现这样的特点：

买入和卖出操作是交替执行的，而且卖出之前一定得先买入。

转化为这样的一个数学问题：

给定一个序列，从该序列中找出一个元素保持在原序列中顺序并且元素个数是偶数的子序列，
使得其偶数项之和与奇数项之和的差最大。

而对于每一天来说，只有两种选择，即选择 操作 或者 不操作。而具体的操作是买入还是卖出得由当前已
经执行的操作数是奇偶性来决定。
所以我们可以从天数递增来地推上去直到第n天。
 
如果用 dp[j] 表示 完成第j次交易时 （由 j-1 转移到 j 必需伴随着一次操作）的最大收益，
则状态转移方程可以写为：

dp[j] = max{dp[j], dp[j-1] + prices[i] * (j%2)?-1:1}

外循环 天数 i 从 0 递推到 size (第 j 次交易不一定发生在哪一天)，内循环 j 从 1 递推到当前
允许的最大操作数：min{2*k, i+1} （i 是 prices 中的 第 i+1 个元素）。

初始条件：dp[0] = 0，dp中的其他值为无穷小（None比任何数值都小）。
另外，有一个优化，当 2*k >= size 时，k 的限制已经形同虚设了，操作数限制已经可以覆盖到每一天
都允许操作，这种情况下还用上述DP效率太低，可以改为没有k限制的贪心版本（把所有上升区段跨度求和即为解）。

由于有了上述优化，所以用DP的情况一定是 2*k < size的情况，这种情况下 用完 2*k 次操作数限制
所得的结果一定等于最优解（虽然不一定实际上进行2*k次操作，因为此时实际上放宽了题目限制条件，
在同一个 i 值，dp[j]可能把这个 i 买入使得当前更优（因为初始值为无穷小），而到了dp[j+1]就把
这个 i 卖出使得当前更优，实际上就相当于不操作，但记录的操作数 j 还是增加了2，所以实际上此时
dp[j]表示的准确的实际含义是 最多完成j次交易时（实际可能不在j次时是最优），放大到全局即为 2*k
 处最优。而又因为 i 是递推上去到 n 的，所以总会有找到 正确的最后一次交易使得在第 i 天dp[2*k]
 最大，而 i 再增加，操作数已经不能增加了（已经到了最大的限制）），所以最后的结果为 dp[2*k]。

http://www.jiuzhang.com/solutions/best-time-to-buy-and-sell-stock-iv/

@author: zeminzhang
"""
class Solution:
    # @return an integer as the maximum profit 
    def maxProfit(self, k, prices):
        size = len(prices)
        if k*2 >= size:
            return self.noKLimit(size, prices)
        dp = [None] * (2*k+1)
        dp[0] = 0
        for i in range(size): # day
            for j in range(1, min(2*k, i+1)+1): # 最大操作数， trasaction*2
                dp[j] = max(dp[j], dp[j-1]+prices[i]*[1, -1][j%2]) # j=1 买入 j＝2 卖出 
        return dp[2*k]
            
    def noKLimit(self, size, prices):
        sum = 0
        for i in range(size - 1):
            if prices[i+1]>prices[i]:
                sum += prices[i+1] - prices[i]
        return sum
