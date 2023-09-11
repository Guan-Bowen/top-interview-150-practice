'''
给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串的第一个匹配项的下标（下标从 0 开始）。如果 needle 不是 haystack 的一部分，则返回  -1 。
'''

class Solution(object):
    def strStr(self, haystack, needle):
        m = len(needle)
        # 构造 next 数组
        nextArray = [0]
        j = 0
        for i in range(1, m):
            while j > 0 and needle[j] != needle[i]: j = nextArray[j - 1]
            if needle[j] == needle[i]: j += 1
            nextArray.append(j)
        
        n = len(haystack)
        # 模式串匹配
        k = 0
        for i in range(n):
            while k > 0 and haystack[i] != needle[k]: k = nextArray[k - 1]
            if haystack[i] == needle[k]: k += 1
            if k == m: return i - k + 1
        return -1

'''
class Solution1(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)
        # 8 ms & 12.8 MB
'''