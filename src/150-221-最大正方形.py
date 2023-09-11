'''
在一个由 '0' 和 '1' 组成的二维矩阵内，找到只包含 '1' 的最大正方形，并返回其面积。
'''
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        # dp[i][j]: 以(i, j) 为右下角的最大 "1" 正方形的边长（该处为 0 时显然边长也是 0）
        # dp(i, j) 处的边长应当考察 dp(i-1, j-1) 位置的值，以及其右、下两行的矩阵值
        # （以下方为例）只需考察 dp(i, j-1)，这个 dp 值代表了这一行有几个连续的 "1"
        #             如果它大于 dp(i-1, j-1)，证明 dp(i-1, j-1) 的值全部纳入了 dp(i, j)
        #             如果它小于 dp(i-1, j-1)，则应当以它为准，切割掉 dp(i-1, j-1) 的多余部分
        # dp(i, j) = 1 + min{dp(i-1, j-1), dp(i, j-1), dp(i-1, j)}, when m(i, j)=1
        #          = 0, when m(i, j)=0
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        res = 0
        for i in range(m): 
            dp[i][0] = int(matrix[i][0])
            if dp[i][0] == 1: res = 1
        for j in range(n): 
            dp[0][j] = int(matrix[0][j])
            if dp[0][j] == 1: res = 1
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
                    res = max(res, dp[i][j])
        return res ** 2
