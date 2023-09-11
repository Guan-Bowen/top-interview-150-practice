'''
给你一个字符串数组 tokens ，表示一个根据 逆波兰表示法 表示的算术表达式。

请你计算该表达式。返回一个表示表达式值的整数。

注意：

有效的算符为 '+'、'-'、'*' 和 '/' 。
每个操作数（运算对象）都可以是一个整数或者另一个表达式。
两个整数之间的除法总是 向零截断 。
表达式中不含除零运算。
输入是一个根据逆波兰表示法表示的算术表达式。
答案及所有中间计算结果可以用 32 位 整数表示。
'''
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stk = []
        for string in tokens:
            if string == '+': 
                a, b = stk[-2], stk[-1]
                stk.pop(); stk.pop(); stk.append(a + b)
            elif string == '-': 
                a, b = stk[-2], stk[-1]
                stk.pop(); stk.pop(); stk.append(a - b)
            elif string == '*': 
                a, b = stk[-2], stk[-1]
                stk.pop(); stk.pop(); stk.append(a * b)
            elif string == '/': 
                a, b = stk[-2], stk[-1]
                tmp = abs(a) // abs(b)
                if a * b < 0: tmp = -tmp
                stk.pop(); stk.pop(); stk.append(tmp)
            else:
                stk.append(int(string))
        return stk[0]