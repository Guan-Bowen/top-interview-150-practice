'''
给定一个 n × n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。

你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要 使用另一个矩阵来旋转图像。
'''
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        lo, hi = 0, n - 1
        while lo < hi:
            for i in range(hi - lo):
                matrix[lo][lo + i], matrix[lo + i][hi], matrix[hi][hi - i], matrix[hi - i][lo] = \
                matrix[hi - i][lo], matrix[lo][lo + i], matrix[lo + i][hi], matrix[hi][hi - i]
            lo, hi = lo + 1, hi - 1