'''
如果在将所有大写字符转换为小写字符、并移除所有非字母数字字符之后，短语正着读和反着读都一样。则可以认为该短语是一个 回文串 。

字母和数字都属于字母数字字符。

给你一个字符串 s，如果它是 回文串 ，返回 true ；否则，返回 false 。
'''

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        string = ''
        for i in range(n):
            if s[i].isalpha() or s[i].isdigit():
                string += s[i]
        string = string.lower()
        m = len(string)
        for i in range(m // 2):
            if string[i] != string[-(i + 1)]: return False
        return True