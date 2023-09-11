'''
给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。

请你设计并实现时间复杂度为 O(n) 的算法解决此问题。
'''

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = dict()
        maxLength = 0
        for num in nums:
            # if num not in d.keys():
            # 尽量不使用 keys() 方法，此处使用该方法则 Timeout
            if num not in d:
                leftLength = d.get(num - 1, 0)
                rightLength = d.get(num + 1, 0)
                totalLength = 1 + leftLength + rightLength
                d[num] = totalLength
                if leftLength != 0: d[num - leftLength] = totalLength
                if rightLength != 0: d[num + rightLength] = totalLength
                maxLength = max(totalLength, maxLength)
        return maxLength
