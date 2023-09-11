'''
给你一个整数数组 citations ，其中 citations[i] 表示研究者的第 i 篇论文被引用的次数。计算并返回该研究者的 h 指数。

根据维基百科上 h 指数的定义：h 代表“高引用次数” ，一名科研人员的 h 指数 是指他（她）至少发表了 h 篇论文，并且每篇论文 至少 被引用 h 次。如果 h 有多种可能的值，h 指数 是其中最大的那个。
'''
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        h = times = 0
        while True:
            cnt = 0
            for c in citations:
                if c >= times: 
                    cnt += 1
                    if cnt >= times: 
                        h = times
                        break
            if cnt < times:
                return h
            times += 1
        return times