'''
给定一个 m x n 的矩阵，如果一个元素为 0 ，则将其所在行和列的所有元素都设为 0 。请使用 原地 算法。
'''
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        zeroRows = set()
        zeroCols = set()
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                aij = matrix[i][j]
                if aij == 0:
                    zeroRows.add(i)
                    zeroCols.add(j)
        for row in zeroRows: 
            for j in range(n): matrix[row][j] = 0
        for col in zeroCols:
            for i in range(m): matrix[i][col] = 0
            