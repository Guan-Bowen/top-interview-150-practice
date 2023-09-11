'''
峰值元素是指其值严格大于左右相邻值的元素。

给你一个整数数组 nums，找到峰值元素并返回其索引。数组可能包含多个峰值，在这种情况下，返回 任何一个峰值 所在位置即可。

你可以假设 nums[-1] = nums[n] = -∞ 。

你必须实现时间复杂度为 O(log n) 的算法来解决此问题。
'''
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        lo, hi = 0, n - 1
        mInf = float('-inf')
        while lo <= hi:
            mid = (hi + lo) // 2
            l = mInf if mid == 0 else nums[mid - 1]
            r = mInf if mid == n - 1 else nums[mid + 1]
            if nums[mid] > l and nums[mid] > r: return mid
            elif nums[mid] > l: lo = mid + 1
            else: hi = mid - 1