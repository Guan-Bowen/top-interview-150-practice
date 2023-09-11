'''
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
'''
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # f(x) = f(x-1) + f(x-2)
        fx = [1, 2]
        for i in range(2, n):
            fxi = fx[i - 1] + fx[i - 2]
            fx.append(fxi)
        return fx[n - 1]