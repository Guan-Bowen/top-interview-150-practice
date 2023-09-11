'''
给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使得出现次数超过两次的元素只出现两次 ，返回删除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。
'''

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        l = len(nums)
        i = 0
        cnt = 1
        if l == 0: return 0

        while i < l:
            if i == 0:
                temp = nums[i]
                i += 1
                cnt = 1
                continue
            if nums[i] == temp:
                if cnt < 2:
                    cnt += 1
                    i += 1
                else:
                    nums.pop(i)
                    l -= 1
            else:
                cnt = 1
                temp = nums[i]
                i += 1

        return len(nums)