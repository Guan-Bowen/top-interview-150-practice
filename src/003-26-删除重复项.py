'''
给你一个 升序排列 的数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。元素的 相对顺序 应该保持 一致 。然后返回 nums 中唯一元素的个数。

考虑 nums 的唯一元素的数量为 k ，你需要做以下事情确保你的题解可以被通过：

更改数组 nums ，使 nums 的前 k 个元素包含唯一元素，并按照它们最初在 nums 中出现的顺序排列。nums 的其余元素与 nums 的大小不重要。
返回 k 。
'''

class Solution1(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        l = len(nums)

        if l == 0: return 0

        while i < l:
            if i == 0:
                i += 1
                continue
            if nums[i] == nums[i-1]:
                nums.pop(i)
                l -= 1
            else:
                i += 1
        
        return len(nums)
        # 1228 ms & 13.08 MB

class Solution2(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        res = []
        l = len(nums)
        if l == 0: 
            return 0

        temp = nums[0]
        res.append(nums[0])
        for i in range(l):
            if i == 0 or nums[i] == temp:
                continue
            res.append(nums[i])
            temp = nums[i]

        for i in range(len(res)):
            nums[i] = res[i]

        return len(res)
        # 20 ms & 14.1 MB