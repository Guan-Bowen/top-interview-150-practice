'''
给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。

找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

返回容器可以储存的最大水量。
'''
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        i, j = 0, n - 1
        maxVolume = (j - i) * min(height[i], height[j])
        while i < j:
            if height[i] <= height[j]: i += 1
            else: j -= 1
            newVolume = (j - i) * min(height[i], height[j])
            if newVolume > maxVolume:
                maxVolume = newVolume
        return maxVolume