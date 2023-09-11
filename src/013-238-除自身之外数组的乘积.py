'''
给你一个整数数组 nums，返回 数组 answer ，其中 answer[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积 。

题目数据 保证 数组 nums之中任意元素的全部前缀元素和后缀的乘积都在  32 位 整数范围内。

请不要使用除法，且在 O(n) 时间复杂度内完成此题。
'''

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = len(nums)
        productLeft = []
        productRight = []
        answer = []
        for i in range(l):
            productLeft.append(0)
            productRight.append(0)
            answer.append(0)
        for i in range(l):
            if i == 0:  productLeft[i] = nums[i]
            else: productLeft[i] = nums[i] * productLeft[i - 1]
        for i in range(l):
            idx = l - i - 1
            if idx == l - 1: productRight[idx] = nums[idx]
            else: productRight[idx] = nums[idx] * productRight[idx + 1] 

        for i in range(l):
            if i == 0 or i == l - 1: continue
            answer[i] = productLeft[i - 1] * productRight[i + 1]
        answer[0] = productRight[1]
        answer[l - 1] = productLeft[l - 2]
        return answer 