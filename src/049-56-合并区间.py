'''
以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。
'''
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(intervals)
        if n == 1: return intervals
        intervals.sort(key=cmp)
        res = []
        lo, hi = intervals[0][0], intervals[0][1]
        for i in range(1, n):
            if intervals[i][0] <= hi: 
                hi = max(hi, intervals[i][1])
            else:
                res.append([lo, hi])
                lo, hi = intervals[i][0], intervals[i][1]
        res.append([lo, max(hi, intervals[n - 1][1])])

        return res

def cmp(interval):
    return interval[0]