'''
给定一个字符串 s 和一个字符串数组 words。 words 中所有字符串 长度相同。

s 中的 串联子串 是指一个包含  words 中所有字符串以任意顺序排列连接起来的子串。

例如，如果 words = ["ab","cd","ef"]， 那么 "abcdef"， "abefcd"，"cdabef"， "cdefab"，"efabcd"， 和 "efcdab" 都是串联子串。 "acdbef" 不是串联子串，因为他不是任何 words 排列的连接。
返回所有串联子串在 s 中的开始索引。你可以以 任意顺序 返回答案。
'''
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        n, m, l = len(words), len(words[0]), len(s)
        pattern = n * m
        wordsDict = {}
        res = []
        for word in words:
            if word not in wordsDict: wordsDict[word] = 1
            else: wordsDict[word] += 1
        for i in range(l - pattern + 1):
            subString = s[i:i + pattern]
            firstStepPassed, secondStepPassed = True, True
            for j in range(n):
                if subString[j * m:(j + 1) * m] not in wordsDict.keys():
                    firstStepPassed = False
                    break
            if not firstStepPassed: 
                continue
            else:
                cd = self.copyDict(wordsDict)
                for j in range(n):
                    cd[subString[j * m:(j + 1) * m]] -= 1
                    if cd[subString[j * m:(j + 1) * m]] < 0: 
                        secondStepPassed = False
                        break

                if secondStepPassed: 
                    res.append(i)
        return res
    
    def copyDict(self, d):
        res = {}
        for key in d.keys():
            res[key] = d[key]
        return res
