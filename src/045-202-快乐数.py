'''
编写一个算法来判断一个数 n 是不是快乐数。

「快乐数」 定义为：

对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。
然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。
如果这个过程 结果为 1，那么这个数就是快乐数。
如果 n 是 快乐数 就返回 true ；不是，则返回 false 。
'''
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        uniSet = set()
        while True:
            s = str(n)
            n, sumValue = len(s), 0
            for i in range(n):
                sumValue += int(s[i]) ** 2
            if sumValue == 1: return True
            elif sumValue in uniSet: return False
            else: uniSet.add(sumValue); n = sumValue