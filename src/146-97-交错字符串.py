'''
给定三个字符串 s1、s2、s3，请你帮忙验证 s3 是否是由 s1 和 s2 交错 组成的。

两个字符串 s 和 t 交错 的定义与过程如下，其中每个字符串都会被分割成若干 非空 子字符串：

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
交错 是 s1 + t1 + s2 + t2 + s3 + t3 + ... 或者 t1 + s1 + t2 + s2 + t3 + s3 + ...
注意：a + b 意味着字符串 a 和 b 连接。
'''
class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        # f(i, j) = {f(i-1,j) && s1[i]=s3[i+j-1]} || {f(i,j-1) && s2[j]=s3[i+j-1]}
        m, n, p = len(s1), len(s2), len(s3)
        if m + n != p: return False
        if m == 0: return s2 == s3
        if n == 0: return s1 == s3
        res = [[False] * (n + 1) for _ in range(m + 1)]
        res[0][0] = True
        for i in range(m + 1):
            for j in range(n + 1):
                if i >= 1 and s1[i - 1] == s3[i + j - 1]: 
                    if not res[i][j]: res[i][j] = res[i - 1][j]
                if j >= 1 and s2[j - 1] == s3[i + j - 1]:
                    if not res[i][j]: res[i][j] = res[i][j - 1]
        return res[-1][-1]