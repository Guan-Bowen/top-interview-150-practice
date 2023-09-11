'''
给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。
'''
class Solution(object):
    def calculate(self, s):
        n = len(s)
        tokens = []
        cache = ''
        sigs = {'+', '-', '(', ')'}
        for i in range(n):
            char = s[i]
            if char == ' ': continue
            elif char in sigs: 
                if cache: tokens.append(cache); cache = ''
                tokens.append(char)
            else: cache += char
        if cache: tokens.append(cache)
        flag = True
        m = len(tokens)
        stk = []
        tokens2 = []
        for i in range(m):
            if (tokens[i] == '+' and flag) or (tokens[i] == '-' and not flag): tokens2.append('+')
            elif (tokens[i] == '+' and not flag) or (tokens[i] == '-' and flag): tokens2.append('-')
            elif tokens[i] == '(':
                if i > 0 and tokens[i - 1] == '-': flag = not flag; stk.append('-')
                else: stk.append('+')
            elif tokens[i] == ')':
                if stk[-1] == '-': flag = not flag
                stk.pop()
            else: tokens2.append(tokens[i])
        n, i, j = len(tokens2), 0, 0
        while i < n - 1:
            if (tokens2[i] == '-' or tokens2[i] == '+') and (tokens2[i + 1] == '+' or tokens2[i + 1] == '-'): tokens2.pop(i); n -= 1
            else: i += 1
        lst = []
        while j < n:
            if tokens2[j] == '+':  lst.append(int(tokens2[j + 1])); j += 1
            elif tokens2[j] == '-': lst.append(-int(tokens2[j + 1])); j += 1
            else: lst.append(int(tokens2[j]))
            j += 1
        return sum(lst)