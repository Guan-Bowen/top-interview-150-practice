'''
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。

此外，你可以假设该网格的四条边均被水包围。
'''
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m, n, res = len(grid), len(grid[0]), 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0': continue
                dfs(grid, i, j)
                res += 1
        return res

def dfs(grid, i, j):
    m, n = len(grid), len(grid[0])
    if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == '0': return
    grid[i][j] = '0'
    dfs(grid, i - 1, j)
    dfs(grid, i + 1, j)
    dfs(grid, i, j - 1)
    dfs(grid, i, j + 1)
