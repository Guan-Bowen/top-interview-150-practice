'''
给定两个字符串 s 和 t ，判断它们是否是同构的。

如果 s 中的字符可以按某种映射关系替换得到 t ，那么这两个字符串是同构的。

每个出现的字符都应当映射到另一个字符，同时不改变字符的顺序。不同字符不能映射到同一个字符上，相同字符只能映射到同一个字符上，字符可以映射到自己本身。
'''
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        n = len(s)
        f1 = {}
        f2 = {}
        for i in range(n):
            if s[i] not in f1.keys(): f1[s[i]] = t[i]
            elif f1[s[i]] != t[i]: return False
            if t[i] not in f2.keys(): f2[t[i]] = s[i]
            elif f2[t[i]] != s[i]: return False
        return True