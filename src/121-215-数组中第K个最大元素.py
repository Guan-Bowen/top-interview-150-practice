'''
给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。

请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

你必须设计并实现时间复杂度为 O(n) 的算法解决此问题。
'''
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        def buildMaxHeap(i, border):
            j = i * 2 + 1
            while j <= border:
                if j + 1 <= border and nums[j] < nums[j + 1]: j = j + 1
                if nums[i] < nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
                    i = j
                    j = i * 2 + 1
                else: break
        
        for i in range(n // 2 - 1, -1, -1):
            buildMaxHeap(i, n - 1)
        for j in range(n - 1, n - k - 1, -1):
            nums[0], nums[j] = nums[j], nums[0]
            buildMaxHeap(0, j - 1)
        return nums[-k]