'''
给你两个单词 word1 和 word2， 请返回将 word1 转换成 word2 所使用的最少操作数  。

你可以对一个单词进行如下三种操作：

插入一个字符
删除一个字符
替换一个字符
'''
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m, n = len(word1), len(word2)
        if m == 0 or n == 0: return max(m, n)
        res = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1): res[i][0] = i
        for j in range(1, n + 1): res[0][j] = j
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # res[i-1][j-1]: w1 和 w2 两词均增加长度 1 —— 对应一个 “改” 操作
                # res[i-1][j]: rij 中只有 w1 短 1 —— 对应一个 “增” 操作
                # res[i][j-1]: 同上，对应一个 “删” 操作
                # 后 +1，代表对应的该次操作，最终结果取三者小值
                res[i][j] = min(res[i - 1][j - 1], res[i - 1][j], res[i][j - 1]) + 1
                # 考虑不需要操作，即 w1 和 w2 在此处的字母相同的情况
                # 此时的 “改” 操作可以省去，即 r[i-1][j-1] 与其他两操作 +1 相比较取小
                if word1[i - 1] == word2[j - 1]:
                    res[i][j] = min(res[i][j], res[i - 1][j - 1])
        return res[-1][-1]