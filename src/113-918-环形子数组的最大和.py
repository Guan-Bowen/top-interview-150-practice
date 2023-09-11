'''
给定一个长度为 n 的环形整数数组 nums ，返回 nums 的非空 子数组 的最大可能和 。

环形数组 意味着数组的末端将会与开头相连呈环状。形式上， nums[i] 的下一个元素是 nums[(i + 1) % n] ， nums[i] 的前一个元素是 nums[(i - 1 + n) % n] 。

子数组 最多只能包含固定缓冲区 nums 中的每个元素一次。形式上，对于子数组 nums[i], nums[i + 1], ..., nums[j] ，不存在 i <= k1, k2 <= j 其中 k1 % n == k2 % n 。
'''
class Solution(object):
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n, total = len(nums), sum(nums)
        mInf = float('-inf')
        dp = [[mInf] * n for _ in range(3)]
        # 三行分别为：
        # (1) dp[0][i] —— 到 i 位置最大的子数组和
        # (2) dp[1][i] —— 到 i 位置最小的子数组和
        # (3) dp[2][i] —— 数组总和 - dp[1][i] —— 整体减去中间，代表了跨越首尾的和值
        dp[0][0] = nums[0]
        dp[1][0] = nums[0]
        dp[2][0] = total - nums[0]
        maxValue1, maxValue2 = dp[0][0], dp[2][0]
        for i in range(1, n):
            dp[0][i] = max(nums[i], nums[i] + dp[0][i - 1])
            dp[1][i] = min(nums[i], nums[i] + dp[1][i - 1])
            dp[2][i] = total - dp[1][i]
            maxValue1 = max(maxValue1, dp[0][i])
            maxValue2 = max(maxValue2, dp[2][i])
        # 如果 maxValue2 = 0，代表取了一个空数组，这种情况舍去，返回 maxValue1
        if maxValue2 > maxValue1 and maxValue2 != 0: return maxValue2
        else: return maxValue1