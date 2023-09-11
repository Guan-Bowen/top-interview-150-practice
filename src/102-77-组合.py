'''
给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。

你可以按 任何顺序 返回答案。
'''
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        def buildResult(i, cache):
            if len(cache) == k: 
                res.append(cache)
                return
            for j in range(i, n + 1):
                buildResult(j + 1, cache + [j])
        
        buildResult(1, [])
        return res