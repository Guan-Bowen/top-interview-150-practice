'''
给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。
'''
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        l1 = [[nums[0]]]
        l2 = []
        for i in range(1, n):
            tar = nums[i]
            for subList in l1:
                for j in range(i + 1):
                    cache = [subList[_] for _ in range(len(subList))]
                    cache.insert(j, tar)
                    l2.append(cache)
            l1 = l2
            l2 = []
        return l1