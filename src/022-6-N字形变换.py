'''
将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。

之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："PAHNAPLSIIGYIR"。

请你实现这个将字符串进行指定行数变换的函数：
'''
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1: return s
        subStrings = []
        for i in range(numRows): subStrings.append('')
        goDown = True
        cursor = 0
        for i in range(len(s)):
            subStrings[cursor] += s[i]
            if cursor == 0: 
                cursor += 1
                goDown = True
            elif cursor == numRows - 1: 
                cursor -= 1
                goDown = False
            else:
                if goDown: cursor += 1
                else: cursor -= 1
        
        return ''.join(subStrings)