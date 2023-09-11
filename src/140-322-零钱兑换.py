'''
给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。

计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。

你可以认为每种硬币的数量是无限的。
'''
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        memo = dict()
        def dp(amt):
            if amt in memo: return memo[amt]
            if amt < 0: return -1
            if amt == 0: return 0
            res = amt + 1
            for coin in coins:
                subRes = dp(amt - coin)
                if subRes == -1: continue
                res = min(res, subRes + 1)
            if res == amt + 1: memo[amt] = -1
            else: memo[amt] = res
            return memo[amt]

        return dp(amount)