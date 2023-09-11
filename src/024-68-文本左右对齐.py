'''
给定一个单词数组 words 和一个长度 maxWidth ，重新排版单词，使其成为每行恰好有 maxWidth 个字符，且左右两端对齐的文本。

你应该使用 “贪心算法” 来放置给定的单词；也就是说，尽可能多地往每行中放置单词。必要时可用空格 ' ' 填充，使得每行恰好有 maxWidth 个字符。

要求尽可能均匀分配单词间的空格数量。如果某一行单词间的空格不能均匀分配，则左侧放置的空格数要多于右侧的空格数。

文本的最后一行应为左对齐，且单词之间不插入额外的空格。

注意:

单词是指由非空格字符组成的字符序列。
每个单词的长度大于 0，小于等于 maxWidth。
输入单词数组 words 至少包含一个单词。
'''
class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        n = len(words)
        res = []
        lo = hi = 0
        i = cnt = 0
        while i != n:
            cnt += len(words[i])
            if cnt > maxWidth: 
                hi = i - 1
                res.append(self.buildSubString(lo, hi, words, maxWidth))
                lo = i
                cnt = 0
                continue
            cnt += 1
            i += 1
        res.append(self.buildSubString(lo, n - 1, words, maxWidth))
        return res
            
    def buildSubString(self, lo, hi, words, width):
        if lo == hi and hi != len(words) - 1:
            return words[lo] + (width - len(words[lo])) * ' '
        elif lo < hi and hi != len(words) - 1:
            spaces = width
            for i in range(lo, hi + 1):
                spaces -= len(words[i])
            avg = spaces // (hi - lo)
            remain = spaces % (hi - lo)
            res = ''
            for i in range(lo, hi + 1):
                res += words[i]
                if remain != 0:
                    res += ' ' * (avg + 1)
                    remain -= 1
                elif i != hi: res += ' ' * avg
            return res
        else:
            res = ''
            for i in range(lo, hi + 1):
                res += words[i]
                if i != hi: res += ' '
            return res + ' ' * (width - len(res))