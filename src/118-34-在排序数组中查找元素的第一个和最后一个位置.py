'''
给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。

如果数组中不存在目标值 target，返回 [-1, -1]。

你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。
'''
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        if not n: return [-1, -1]
        lo, hi = 0, n - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                l1, h1, l2, h2 = lo, mid, mid, hi
                while l1 < h1:
                    m1 = (l1 + h1) // 2
                    if nums[m1] != target: l1 = m1 + 1
                    else: h1 = m1
                while l2 < h2:
                    m2 = (l2 + h2) // 2
                    if nums[m2] == target: 
                        if l2 == m2: 
                            if h2 > l2 and nums[h2] == target: l2 = h2
                            break
                        else: l2 = m2
                    else: h2 = m2 - 1
                return [h1, l2]
            elif nums[mid] > target: hi = mid - 1
            else: lo = mid + 1
        return [-1, -1]