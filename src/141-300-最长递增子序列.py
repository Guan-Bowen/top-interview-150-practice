'''
给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。

子序列 是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。
'''
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0: return 0
        res = [1]
        for i in range(n):
            res.append(1)
            # 对于每一个数字，考察它前面的数字
            # 如果数字比它小，则考察该数字的 res[j] + 1 和当前 res[i] 的情况
            for j in range(i):
                if nums[j] < nums[i]: res[i] = max(res[i], res[j] + 1)
        return max(res)