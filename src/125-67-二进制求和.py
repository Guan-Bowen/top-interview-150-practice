'''
给你两个二进制字符串 a 和 b ，以二进制字符串的形式返回它们的和。
'''
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        la, lb = len(a), len(b)
        i = 0
        res = ''
        step = 0
        while i < max(la, lb):
            xa, xb = 0, 0
            idx = -i - 1
            if i < la: xa = int(a[idx])
            if i < lb: xb = int(b[idx])
            s = xa + xb + step
            if s >= 2:
                s -= 2
                step = 1
            else: step = 0
            res = str(s) + res
            i += 1
        if step: res = '1' + res
        return res