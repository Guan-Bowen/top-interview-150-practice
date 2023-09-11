'''
给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。
'''
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m, n, x, y = len(matrix), len(matrix[0]), 0, 0
        size = m * n
        wall = {}
        wall['left'], wall['right'], wall['top'], wall['bottom'] = -1, n, -1, m
        dirction = 'right'
        res = [matrix[0][0]]
        reached = 1
        while True:
            if dirction == 'right':
                if y + 1 < wall['right']: 
                    y += 1; res.append(matrix[x][y]); reached += 1
                else: 
                    dirction = 'bottom'; wall['top'] += 1
            elif dirction == 'bottom':
                if x + 1 < wall['bottom']:
                    x += 1; res.append(matrix[x][y]); reached += 1
                else:
                    dirction = 'left'; wall['right'] -= 1
            elif dirction == 'left':
                if y - 1 > wall['left']:
                    y -= 1; res.append(matrix[x][y]); reached += 1
                else:
                    dirction = 'top'; wall['bottom'] -= 1
            elif dirction == 'top':
                if x - 1 > wall['top']:
                    x -= 1; res.append(matrix[x][y]); reached += 1
                else:
                    dirction = 'right'; wall['left'] += 1
            if reached == size: break
        return res