'''
给定一个三角形 triangle ，找出自顶向下的最小路径和。

每一步只能移动到下一行中相邻的结点上。相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。也就是说，如果正位于当前行的下标 i ，那么下一步可以移动到下一行的下标 i 或 i + 1 。
'''
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        # f(x, y) = T(x, y) + min{f(x-1, y-1), f(x-1, y)} (If Exists)
        m = len(triangle)
        res = []
        inf = 1e+7 # 最大值 200 * 1e+4 = 2e+6
        for i in range(1, m + 1): res.append([inf] * i)
        res[0][0] = triangle[0][0]
        for i in range(1, m):
            for j in range(i + 1):
                value1 = res[i - 1][j - 1] if j != 0 else inf
                value2 = res[i - 1][j] if j != i else inf
                res[i][j] = triangle[i][j] + min(value1, value2)
        return min(res[m - 1])