'''
给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

子数组 是数组中的一个连续部分。
'''
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        mInf = float('-inf')
        dp = [mInf] * n
        dp[0] = nums[0]
        maxValue = dp[0]
        for i in range(1, n):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
            maxValue = max(maxValue, dp[i])
        return maxValue