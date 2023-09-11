'''
给你一个整数数组 prices 和一个整数 k ，其中 prices[i] 是某支给定的股票在第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。也就是说，你最多可以买 k 次，卖 k 次。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
'''
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        # 原理同（123）买卖股票的最佳时机 III
        inf = 1e+6
        n, lp = 2 * k + 1, len(prices)
        dp = [-inf for _ in range(n)]
        dp[0] = 0
        dp[1] = -prices[0]
        for i in range(lp):
            for j in range(1, n):
                # 奇数位为买入位，偶数位为卖出位
                if j % 2: dp[j] = max(dp[j], dp[j - 1] - prices[i])
                else: dp[j] = max(dp[j], dp[j - 1] + prices[i])
        return max(dp[-1], 0)