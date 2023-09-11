'''
给你一个非负整数 x ，计算并返回 x 的 算术平方根 。

由于返回类型是整数，结果只保留 整数部分 ，小数部分将被 舍去 。

注意：不允许使用任何内置指数函数和算符，例如 pow(x, 0.5) 或者 x ** 0.5 。
'''

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0 or x == 1: return x
        lo, hi = 0, x
        while lo < hi:
            mid = (lo + hi) // 2
            if mid == lo: break
            val = mid * mid
            if val == x: return mid
            elif val < x: lo = mid
            else: hi = mid
        return lo