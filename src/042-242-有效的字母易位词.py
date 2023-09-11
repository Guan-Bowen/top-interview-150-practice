'''
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

注意：若 s 和 t 中每个字符出现的次数都相同，则称 s 和 t 互为字母异位词。
'''
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        m, n = len(s), len(t)
        if m != n: return False
        dictS = {}
        for i in range(n):
            if s[i] in dictS.keys(): dictS[s[i]] += 1
            else:dictS[s[i]] = 1
        for i in range(n):
            if t[i] not in dictS.keys() or dictS[t[i]] <= 0: return False
            else: dictS[t[i]] -= 1
        return True