'''
给你一个 m x n 的矩阵 board ，由若干字符 'X' 和 'O' ，找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。
'''
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        remain = []
        for i in range(m):
            sub = []
            for j in range(n): sub.append(False)
            remain.append(sub)
        for i in range(n):
            if board[0][i] == 'O' and not remain[0][i]: dfs(board, remain, 0, i)
            if board[m - 1][i] == 'O' and not remain[m - 1][i]: dfs(board, remain, m - 1, i)
        for i in range(m):
            if board[i][0] == 'O' and not remain[i][0]: dfs(board, remain, i, 0)
            if board[i][n - 1] == 'O' and not remain[i][n - 1]: dfs(board, remain, i, n - 1)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and not remain[i][j]: board[i][j] = 'X'

def dfs(board, remain, i, j):
    m, n = len(board), len(board[0])
    if i < 0 or i >= m or j < 0 or j >= n or remain[i][j] or board[i][j] == 'X': return
    remain[i][j] = True
    dfs(board, remain, i, j + 1)
    dfs(board, remain, i, j - 1)
    dfs(board, remain, i + 1, j)
    dfs(board, remain, i - 1, j)