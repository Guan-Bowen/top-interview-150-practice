'''
给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。
'''
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n == 0: return 0
        if n == 1: return 1
        lo = hi = value = res = 0
        alphas = set()
        while hi < n:
            if s[hi] not in alphas:
                alphas.add(s[hi])
                value += 1
                res = max(res, value)
                hi += 1
            else:
                lo += 1
                alphas.remove(s[lo - 1])
                value -= 1
        return res