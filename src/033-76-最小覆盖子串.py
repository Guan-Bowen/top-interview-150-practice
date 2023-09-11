'''
给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。
'''

# Timeout at 265 / 267
class Solution1(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        ns, nt = len(s), len(t)
        if ns < nt: return ''
        dt = {}
        for i in range(nt):
            if t[i] not in dt.keys(): dt[t[i]] = 1
            else: dt[t[i]] += 1
        
        lo, hi, length, res = 0, nt - 1, 2 * 10e+5, ''
        while hi < ns:
            if hi - lo + 1 < nt: hi += 1
            elif hi - lo + 1 >= length or (s[lo] not in dt.keys()): lo += 1
            else:
                subString = s[lo:hi + 1]
                flag = True
                for key in dt.keys():
                    if subString.count(key) < dt[key]:
                        flag = False
                        break
                if flag and len(subString) < length:
                    length = len(subString)
                    res = subString
                    lo += 1
                else: 
                    hi += 1
                    while hi < ns and s[hi] not in dt.keys():
                        hi += 1
        return res