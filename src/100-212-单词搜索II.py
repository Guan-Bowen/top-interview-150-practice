'''
给定一个 m x n 二维字符网格 board 和一个单词（字符串）列表 words， 返回所有二维网格上的单词 。

单词必须按照字母顺序，通过 相邻的单元格 内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在一个单词中不允许被重复使用。
'''
class Trie(object):
    def __init__(self):
        self.child = dict()
        self.isWord = False

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        m, n = len(board), len(board[0])
        res = []
        tr = Trie()
        for word in words:
            node = tr
            for char in word:
                if char not in node.child: node.child[char] = Trie()
                node = node.child[char]
            node.isWord = True

        
        def dfs(x, y, node, path):
            if x < 0 or x >= m or y < 0 or y >= n: return
            char = board[x][y]
            if char == '$' or char not in node.child: return
            if ((node.child)[char]).isWord: res.append(path + char)
            # 如果 Trie 已经没有字节点了，直接返回，停止搜索（不剪枝超时）
            if not (node.child[char]).child: return
            board[x][y] = '$' # 已达到该字符
            for i, j in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                dfs(i, j, (node.child)[char], path + char)
            board[x][y] = char # 退出该处 dfs 时，复原已达标记

        for i in range(m):
            for j in range(n):
                dfs(i, j, tr, '')
        return list(set(res))