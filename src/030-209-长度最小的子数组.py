'''
给定一个含有 n 个正整数的数组和一个正整数 target 。

找出该数组中满足其和 ≥ target 的长度最小的 连续子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。
'''

class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            if nums[0] >= target: return 1
            else: return 0
        lo, hi, sumVal = 0, 0, 0
        res = 2 * 10e+5
        exist = False
        enlarged = True
        while hi < n:
            if enlarged: sumVal += nums[hi]
            else: sumVal -= nums[lo - 1]
            if sumVal >= target:
                delta = hi - lo + 1
                if delta < res: res = delta; exist = True
                if res == 1: return 1
                lo += 1
                enlarged = False
            else:
                hi += 1
                enlarged = True

        if not exist: return 0
        else: return res