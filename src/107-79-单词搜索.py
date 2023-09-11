'''
给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
'''
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m, n, length = len(board), len(board[0]), len(word)
        reached = [[False for _ in range(n)] for _ in range(m)]
        def dfs(x, y, curr):
            if x < 0 or x >= m or y < 0 or y >= n or reached[x][y]: return False
            if board[x][y] == word[curr]:
                if curr == length - 1: return True
                reached[x][y] = True
                res = dfs(x + 1, y, curr + 1) or dfs(x - 1, y, curr + 1) or dfs(x, y + 1, curr + 1) or dfs(x, y - 1, curr + 1)
                if res: return True
                else:
                    reached[x][y] = False
                    return False
            else: return False

        for i in range(m):
            for j in range(n):
                res = dfs(i, j, 0)
                if res: return True
        return False