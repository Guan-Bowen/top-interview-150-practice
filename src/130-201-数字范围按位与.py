'''
给你两个整数 left 和 right ，表示区间 [left, right] ，返回此区间内所有数字 按位与 的结果（包含 left 、right 端点）。
'''
class Solution(object):
    def rangeBitwiseAnd(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        # 连续与运算：等价于寻找最大公共前缀
        # 中间变换的部分只要出现一个 0，则该位置的结果为 0
        # 结果是除 left 和 right 的最大前缀外全部为 0
        shift = 0
        while left < right:
            left = left >> 1
            right = right >> 1
            shift += 1
        return left << shift