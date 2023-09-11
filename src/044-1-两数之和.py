'''
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。
'''
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        temp = sorted(nums)
        n = len(nums)
        lo, hi = 0, n - 1
        while lo < hi:
            sumValue = temp[lo] + temp[hi]
            if sumValue == target: 
                idx1, idx2 = nums.index(temp[lo]), nums.index(temp[hi])
                if idx1 == idx2:
                    nums.reverse()
                    idx2 = n - 1 - nums.index(temp[hi])
                return [min(idx1, idx2), max(idx1, idx2)]
            if sumValue < target: lo += 1
            else: hi -= 1
