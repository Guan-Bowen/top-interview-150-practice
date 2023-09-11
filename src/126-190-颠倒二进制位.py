'''
颠倒给定的 32 位无符号整数的二进制位。
'''
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        s = (str(bin(n)))[2:]
        ls = len(s)
        s = s[::-1] + (32 - ls) * '0'
        res = 0
        for i in range(32):
            res += int(s[i]) * 2 ** (31 - i)
        return res