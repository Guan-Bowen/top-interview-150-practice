'''
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
'''
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        base = ['()']
        temp = []
        if n == 1: return base
        for i in range(2, n + 1):
            for s in base:
                ls = list(s)
                sz = len(ls)
                for j in range(sz + 1):
                    ls2 = [ls[_] for _ in range(sz)]
                    ls2.insert(j, '(')
                    for k in range(j + 1, sz + 2):
                        ls3 = [ls2[_] for _ in range(sz + 1)]
                        ls3.insert(k, ')')
                        temp.append(''.join(ls3))
            base = list(set(temp))
            temp = []
        return base