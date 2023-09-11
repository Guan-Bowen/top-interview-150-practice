'''
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
每个右括号都有一个对应的相同类型的左括号。
'''

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stk = []
        for char in s:
            if char == '(' or char == '[' or char == '{': stk.append(char)
            elif char == ')':
                if not stk or stk[-1] != '(': return False
                else: stk.pop()
            elif char == ']':
                if not stk or stk[-1] != '[': return False
                else: stk.pop()
            elif char == '}':
                if not stk or stk[-1] != '{': return False
                else: stk.pop()
        if stk: return False
        return True
        