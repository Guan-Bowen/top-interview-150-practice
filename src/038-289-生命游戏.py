'''
给定一个包含 m × n 个格子的面板，每一个格子都可以看成是一个细胞。每个细胞都具有一个初始状态： 1 即为 活细胞 （live），或 0 即为 死细胞 （dead）。每个细胞与其八个相邻位置（水平，垂直，对角线）的细胞都遵循以下四条生存定律：

如果活细胞周围八个位置的活细胞数少于两个，则该位置活细胞死亡；
如果活细胞周围八个位置有两个或三个活细胞，则该位置活细胞仍然存活；
如果活细胞周围八个位置有超过三个活细胞，则该位置活细胞死亡；
如果死细胞周围正好有三个活细胞，则该位置死细胞复活；
下一个状态是通过将上述规则同时应用于当前状态下的每个细胞所形成的，其中细胞的出生和死亡是同时发生的。给你 m x n 网格面板 board 的当前状态，返回下一个状态。
'''

class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        Exist = []
        for i in range(m):
            Exist.append([])
            for j in range(n):
                if board[i][j] == 0: Exist[i].append(False)
                else: Exist[i].append(True)
        for i in range(m):
            for j in range(n):
                cnt = 0
                if i - 1 >= 0:
                    if j - 1 >= 0 and board[i - 1][j - 1] == 1: cnt += 1
                    if j + 1 < n and board[i - 1][j + 1] == 1: cnt += 1
                    if board[i - 1][j] == 1: cnt += 1
                if i + 1 < m:
                    if j - 1 >= 0 and board[i + 1][j - 1] == 1: cnt += 1
                    if j + 1 < n and board[i + 1][j + 1] == 1: cnt += 1
                    if board[i + 1][j] == 1: cnt += 1
                if j - 1 >= 0 and board[i][j - 1] == 1: cnt += 1
                if j + 1 < n and board[i][j + 1] == 1: cnt += 1

                if Exist[i][j] and cnt < 2: Exist[i][j] = False
                elif Exist[i][j] and cnt <= 3: Exist[i][j] = True
                elif Exist[i][j] and cnt > 3: Exist[i][j] = False
                elif not Exist[i][j] and cnt == 3: Exist[i][j] = True

        for i in range(m):
            for j in range(n):
                if Exist[i][j]: board[i][j] = 1
                else: board[i][j] = 0        