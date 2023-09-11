'''
给你两个字符串：ransomNote 和 magazine ，判断 ransomNote 能不能由 magazine 里面的字符构成。

如果可以，返回 true ；否则返回 false 。

magazine 中的每个字符只能在 ransomNote 中使用一次。
'''

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        lenRansom, lenMagazine = len(ransomNote), len(magazine)
        dictMagazine = {}
        for i in range(lenMagazine):
            if magazine[i] in dictMagazine.keys(): dictMagazine[magazine[i]] += 1
            else: dictMagazine[magazine[i]] = 1
        for j in range(lenRansom):
            if ransomNote[j] not in dictMagazine.keys() or dictMagazine[ransomNote[j]] <= 0:
                return False
            else: dictMagazine[ransomNote[j]] -= 1
        return True
