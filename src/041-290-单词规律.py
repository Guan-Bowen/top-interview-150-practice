'''
给定一种规律 pattern 和一个字符串 s ，判断 s 是否遵循相同的规律。

这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 s 中的每个非空单词之间存在着双向连接的对应规律。
'''
class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        listPtn = list(pattern)
        listS = s.split(' ')
        n, m = len(listPtn), len(listS)
        if n != m: return False
        f1 = {}
        f2 = {}
        for i in range(n):
            if listPtn[i] not in f1.keys(): f1[listPtn[i]] = listS[i]
            elif f1[listPtn[i]] != listS[i]: return False
            if listS[i] not in f2.keys():f2[listS[i]] = listPtn[i]
            elif f2[listS[i]] != listPtn[i]: return False
        return True