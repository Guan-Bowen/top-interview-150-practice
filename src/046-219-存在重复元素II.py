'''
给你一个整数数组 nums 和一个整数 k ，判断数组中是否存在两个 不同的索引 i 和 j ，满足 nums[i] == nums[j] 且 abs(i - j) <= k 。如果存在，返回 true ；否则，返回 false 。
'''
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        n = len(nums)
        if len(set(nums)) == n: return False
        if k >= n: return n > len(set(nums))
        for i in range(n - k):
            s = set(nums[i:i + k + 1])
            if len(s) < k + 1: return True
        return False