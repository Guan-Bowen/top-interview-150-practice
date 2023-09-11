'''
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish”）。

现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？

网格中的障碍物和空位置分别用 1 和 0 来表示。
'''
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        # f(x, y) = f(x-1, y) + f(x, y-1), when oG(x, y)=0
        #         = 0, when oG(x, y)=1
        # [首行首列单独初始化]
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        res = [[0] * n for _ in range(m)]
        res[0][0] = 1 - obstacleGrid[0][0]
        for i in range(1, n): 
            if not obstacleGrid[0][i]: res[0][i] = res[0][i - 1]
            else: break
        for j in range(1, m):
            if not obstacleGrid[j][0]: res[j][0] = res[j - 1][0]
            else: break
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1: res[i][j] = 0
                else: res[i][j] = res[i - 1][j] + res[i][j - 1]
        return res[m - 1][n - 1]