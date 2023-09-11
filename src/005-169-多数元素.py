'''
给定一个大小为 n 的数组 nums ，返回其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。
'''

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        max_times = len(nums) // 2

        for i in range(len(nums)):
            if not d.has_key(nums[i]):
                d[nums[i]] = nums.count(nums[i])
        
        for key in d.keys():
            if d[key] > max_times:
                return key