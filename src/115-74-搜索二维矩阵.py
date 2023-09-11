'''
给你一个满足下述两条属性的 m x n 整数矩阵：

每行中的整数从左到右按非递减顺序排列。
每行的第一个整数大于前一行的最后一个整数。
给你一个整数 target ，如果 target 在矩阵中，返回 true ；否则，返回 false 。
'''
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # 二维的二分查找
        if matrix[0][0] > target or matrix[-1][-1] < target: return False
        m, n = len(matrix), len(matrix[0])
        lo, hi = 0, m - 1
        while lo < hi:
            curr = (lo + hi) // 2
            if matrix[curr][0] < target and matrix[curr + 1][0] <= target: lo = curr + 1
            else: hi = curr
        ptr = lo
        lo, hi = 0, n - 1
        while lo < hi:
            curr = (lo + hi) // 2
            if matrix[ptr][curr] < target: lo = curr + 1
            else: hi = curr
        return target == matrix[ptr][lo]