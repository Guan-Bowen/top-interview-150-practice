'''
给定一个整数 n ，返回 n! 结果中尾随零的数量。

提示 n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1
'''
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        '''
        val = 1
        for i in range(1, n + 1): val *= i
        s = str(val)
        l = len(s)
        res = 0
        for i in range(l): 
            if s[l - i - 1] == '0': res += 1
            else: break
        return res
        '''
        # 求因子 5 的个数
        res = 0
        while n >= 5:
            res += n // 5
            n //= 5
        return res