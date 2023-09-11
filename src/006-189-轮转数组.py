'''
给定一个整数数组 nums，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。
'''

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        k %= l
        res = nums[-k:] + nums[0:-k]

        for i in range(l):
            nums[i] = res[i]
        # 40 ms & 25.52 MB