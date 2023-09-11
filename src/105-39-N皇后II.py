'''
n 皇后问题 研究的是如何将 n 个皇后放置在 n × n 的棋盘上，并且使皇后彼此之间不能相互攻击。

给你一个整数 n ，返回 n 皇后问题 不同的解决方案的数量。
'''
class Solution(object):
    def __init__(self):
        self.res = 0
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 处于同一个对角线上：i+j 相等或 i-j 相等
        col = set()     # 保存 j
        cross1 = set()  # 保存 i+j
        cross2 = set()  # 保存 i-j
        def trace(i):
            if i == n: 
                self.res += 1
                return
            for j in range(n):
                if j not in col and i + j not in cross1 and i - j not in cross2:
                    col.add(j)
                    cross1.add(i + j)
                    cross2.add(i - j)
                    trace(i + 1)
                    col.remove(j)
                    cross1.remove(i + j)
                    cross2.remove(i - j)
        trace(0)
        return self.res