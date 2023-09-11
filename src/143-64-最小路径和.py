'''
给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。
'''
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # f(x, y) = G(x, y) + min{f(x-1, y), f(x, y-1)} (If Exists)
        # 最大值约为 (200 + 200) * 200 = 8e+4
        m, n = len(grid), len(grid[0])
        inf = 1e+5
        # 这里如果使用 [[inf] * n] * m 会有浅拷贝问题
        res = [[inf] * n for _ in range(m)]
        res[0][0] = grid[0][0]
        # 最上行和最左列的初始化，这两部分到达相应的点只有一种走法
        for i in range(1, n): res[0][i] = res[0][i - 1] + grid[0][i]
        for j in range(1, m): res[j][0] = res[j - 1][0] + grid[j][0]
        for i in range(1, m):
            for j in range(1, n):
                res[i][j] = grid[i][j] + min(res[i - 1][j], res[i][j - 1])
        return res[m - 1][n - 1]