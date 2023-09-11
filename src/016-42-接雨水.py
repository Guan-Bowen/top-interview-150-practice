'''
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
'''
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        leftHighest = []
        rightHightest = []
        l = len(height)
        for i in range(l):
            leftHighest.append(0)
            rightHightest.append(0)
        for i in range(l):
            if i == 0: continue
            leftHighest[i] = max(leftHighest[i - 1], height[i - 1])
            rightHightest[l - i - 1] = max(rightHightest[l - i], height[l - i])
        # print leftHighest
        # print rightHightest
        res = 0
        for i in range(l):
            borderHeight = min(leftHighest[i], rightHightest[i])
            if borderHeight > height[i]: res += borderHeight - height[i]
        return res