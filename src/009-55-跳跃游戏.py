'''
给定一个非负整数数组 nums ，你最初位于数组的 第一个下标 。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个下标。
'''

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        canReached = 0
        for i in range(len(nums)):
            if canReached < i:
                return False
            canReached = max(canReached, i + nums[i])
        
        return True