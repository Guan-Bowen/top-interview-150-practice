'''
给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
'''
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        inf = 1e+6
        dp = [0, -prices[0], -inf, -inf, -inf]
        # 只有五种状态 —— dp0~4: 无操作，买一次，买卖各一次，买两次卖一次，买卖各两次
        # dp1 更新第一次买对应的最低价格（收益最大的负值）
        # dp2 更新买卖一次的最大收
        # dp3 更新买卖一次之后再买的最大收
        # dp4 更新买卖两次的最大收益
        for i in range(1, len(prices)):
            dp[1] = max(dp[1], dp[0] - prices[i])
            dp[2] = max(dp[2], dp[1] + prices[i])
            dp[3] = max(dp[3], dp[2] - prices[i])
            dp[4] = max(dp[4], dp[3] + prices[i])
        return max(dp[4], 0)