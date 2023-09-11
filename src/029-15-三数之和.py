'''
给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请

你返回所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。
'''

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        n = len(nums)
        res = []
        for i in range(1, n-1):
            lo, hi = i - 1, i + 1
            while True:
                sum3 = nums[lo] + nums[i] + nums[hi]
                if sum3 == 0: 
                    res.append([nums[lo], nums[i], nums[hi]])
                    lo, hi = lo - 1, hi + 1
                elif sum3 > 0: lo -= 1
                else: hi += 1
                if lo < 0 or hi > n - 1: break
        res2 = []
        for r in res: 
            if r not in res2: res2.append(r)

        return res2