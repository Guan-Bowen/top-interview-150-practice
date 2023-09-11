'''
编写一个函数，输入是一个无符号整数（以二进制串的形式），返回其二进制表达式中数字位数为 '1' 的个数（也被称为汉明重量）。
'''
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = (str(bin(n)))[2:]
        cnt = 0
        for i in range(len(s)):
            if s[i] == '1': cnt += 1
        return cnt