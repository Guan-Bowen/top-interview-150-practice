'''
实现 pow(x, n) ，即计算 x 的整数 n 次幂函数（即，xn ）。
'''

class Solution(object):
    def myPow(self, x, n):
        if x == 0.0: return x
        if n < 0: x, n = 1.0 / x, -n
        res = 1
        while n:
            if n & 1: res *= x
            n //= 2
            x *= x
        
        return res
        
class Solution1(object):
    def myPow(self, x, n):
        if x == 0.0: return x
        if n < 0: x, n = 1.0 / x, -n
        res = 1
        while n:
            if n % 2: res *= x # 如果 x 是一个奇数，则需要多乘一个 x，补偿取整的舍去
            n //= 2
            x *= x
        
        return res