'''
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。
'''

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 走到第 k 个房子处，有两种选择：偷与不偷
        # 如果不偷，则与前 k-1 收益一致，否则为前 k-2 并当前房间的收益
        # f(k) = max{f(k-1), f(k-2) + H(k)}
        n = len(nums)
        if n == 1: return nums[0]
        if n == 2: return max(nums[0], nums[1])
        profit = [nums[0], max(nums[0], nums[1])]
        for k in range(2, n):
            profit.append(max(profit[k - 1], profit[k - 2] + nums[k]))
        return profit[-1]