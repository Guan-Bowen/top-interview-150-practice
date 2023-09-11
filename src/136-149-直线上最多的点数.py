'''
给你一个数组 points ，其中 points[i] = [xi, yi] 表示 X-Y 平面上的一个点。求最多有多少个点在同一条直线上。
'''
class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)
        if n == 1: return 1
        checked = set() # 规避已经确定直线归属的点，以规避 Timeout
        res = 2
        for i in range(n):
            for j in range(i + 1, n):
                cnt = 2
                deltaX, deltaY = points[j][0] - points[i][0], points[j][1] - points[i][1]
                for k in range(j + 1, n):
                    if (i, j) in checked or (j, k) in checked or (i, k) in checked:
                        continue
                    deltaX2, deltaY2 = points[j][0] - points[k][0], points[j][1] - points[k][1]
                    if deltaX * deltaY2 == deltaY * deltaX2: # dy/dx = dy2/dx2
                        checked.add((j, k))
                        checked.add((i, k))
                        cnt += 1
                res = max(res, cnt)
        return res