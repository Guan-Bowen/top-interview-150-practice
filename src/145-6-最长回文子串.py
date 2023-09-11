'''
给你一个字符串 s，找到 s 中最长的回文子串。

如果字符串的反序与原始字符串相同，则该字符串称为回文字符串。
'''
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # f(i, j) = f(i - 1, j + 1) && s[i]=s[j] (边界特殊处理)
        length = len(s)
        if length == 1: return s
        if length == 2: return s if s[0] == s[1] else s[0]
        maxLen = 1
        startPoint = 0
        res = [[False] * length for _ in range(length)]
        for i in range(length): res[i][i] = True
        # 为了保证在串长度大于 3 的情况下 res[i+1][j-1]（左下角）存在
        # 选择 j-i 的遍历方式
        for j in range(1, length):
            for i in range(j):
                # 长度为 2，3 的串，只需要检查首尾字符
                if j - i <= 2 and s[i] == s[j]: 
                    res[i][j] = True
                    prLen = j - i + 1
                # 长度大于 3 的，检查首尾字符，以及 res[i+1][j-1]
                elif res[i + 1][j - 1] and s[i] == s[j]:
                    res[i][j] = True
                    prLen = j - i + 1
                if res[i][j] and prLen > maxLen:
                    startPoint = i
                    maxLen = prLen
        return s[startPoint:startPoint+maxLen]