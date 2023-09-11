'''
给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。

你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。

返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。
'''
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        minPrice = float('inf')
        maxPro = 0

        for price in prices:
            # 更新从第一日到当日的最低价格
            minPrice = min(price, minPrice)
            # 更新当日可以达到的最大收益，有两种可能：
            # (1) 当日的价格与最低价之差最大
            # (2) 当日的价格无影响，前一天的最大收益最大
            maxPro = max(maxPro, price - minPrice)
        
        return maxPro