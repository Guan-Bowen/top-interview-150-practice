'''
给你一个字符串 s ，请你反转字符串中 单词 的顺序。

单词 是由非空格字符组成的字符串。s 中使用至少一个空格将字符串中的 单词 分隔开。

返回 单词 顺序颠倒且 单词 之间用单个空格连接的结果字符串。

注意：输入字符串 s中可能会存在前导空格、尾随空格或者单词间的多个空格。返回的结果字符串中，单词间应当仅用单个空格分隔，且不包含任何额外的空格。
'''
class Solution(object):
    def reverseWords(self, s):
        words = s.split()
        words.reverse()
        return ' '.join(words)
        # 16 ms & 13.2 MB


class Solution1(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = []
        start = 0
        while True:
            if s == '': break
            reachingWord = False
            cache = ''
            while s and (s[0] != ' ' or not reachingWord):
                if s[0] == ' ': s = s[1:]
                else:
                    reachingWord = True
                    cache += s[0]
                    s = s[1:]
            if reachingWord: words.append(cache)
        words.reverse()
        res = ''
        for i in range(len(words)):
            res += words[i]
            if i < len(words) - 1: res += ' '
        return res
        # 40 ms & 13.1 MB