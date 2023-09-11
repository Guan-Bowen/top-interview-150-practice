'''
给你一个 非空 整数数组 nums ，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

你必须设计并实现线性时间复杂度的算法来解决此问题，且该算法只使用常量额外空间。
'''
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        # 异或满足交换律
        # 相同数字的按位异或结果为 0
        # 0 与 一个二进制数字按位异或，结果等于这个数本身
        for i in range(len(nums)):
            res = res ^ nums[i]
        return res