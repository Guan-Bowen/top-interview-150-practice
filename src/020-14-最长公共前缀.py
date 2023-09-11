'''
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。
'''
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ''
        loops = 201
        for string in strs:
            if loops > len(string): loops = len(string)
        res = ''
        for i in range(loops):
            flag = True
            s = strs[0][i]
            for string in strs:
                if string[i] != s: flag = False; break
            if flag: res += s
            else: break
        return res