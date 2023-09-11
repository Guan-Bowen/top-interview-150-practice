'''
给你一个变量对数组 equations 和一个实数值数组 values 作为已知条件，其中 equations[i] = [Ai, Bi] 和 values[i] 共同表示等式 Ai / Bi = values[i] 。每个 Ai 或 Bi 是一个表示单个变量的字符串。

另有一些以数组 queries 表示的问题，其中 queries[j] = [Cj, Dj] 表示第 j 个问题，请你根据已知条件找出 Cj / Dj = ? 的结果作为答案。

返回 所有问题的答案 。如果存在某个无法确定的答案，则用 -1.0 替代这个答案。如果问题中出现了给定的已知条件中没有出现的字符串，也需要用 -1.0 替代这个答案。

注意：输入总是有效的。你可以假设除法运算中不会出现除数为 0 的情况，且不存在任何矛盾的结果。

注意：未在等式列表中出现的变量是未定义的，因此无法确定它们的答案。
'''
class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        g = defaultdict(dict)
        for (a, b), v in zip(equations, values): g[a][b], g[b][a] = v, 1 / v

        for k in g:
            for i in g:
                for j in g:
                    if k in g[i] and j in g[k]:
                        g[i][j] = g[i][k] * g[k][j]

        return [g[a][b] if a in g and b in g[a] else -1.0 for a, b in queries]