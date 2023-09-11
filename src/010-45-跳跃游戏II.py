'''
给定一个长度为 n 的 0 索引整数数组 nums。初始位置为 nums[0]。

每个元素 nums[i] 表示从索引 i 向前跳转的最大长度。换句话说，如果你在 nums[i] 处，你可以跳转到任意 nums[i + j] 处:

0 <= j <= nums[i] 
i + j < n
返回到达 nums[n - 1] 的最小跳跃次数。生成的测试用例可以到达 nums[n - 1]。
'''

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length == 0 or length == 1: 
            return 0

        lo = 0
        hi = 0
        count = 1

        # 计算第 count 步可达的范围区间：
        # (1) 下一步区间的起点为此一步区间的下一点（更小的本步就可达）
        # (2) 下一步区间的终点为此一步每一点可达终点的最大者
        while True:
            maxVal = hi + 1
            for i in range(lo, hi + 1):
                maxVal = max(maxVal, nums[i] + i)

            if maxVal >= length - 1:
                return count
            lo = hi + 1
            hi = maxVal
            count += 1
        