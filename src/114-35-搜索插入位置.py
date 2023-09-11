'''
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

请必须使用时间复杂度为 O(log n) 的算法。
'''
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            curr = (lo + hi) // 2
            if nums[curr] == target: return curr
            elif nums[curr] < target: 
                if lo == curr: lo += 1
                else: lo = curr
            else: hi = curr
        if nums[lo] >= target: return lo
        else: return lo + 1