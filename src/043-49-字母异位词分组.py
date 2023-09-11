'''
给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。

字母异位词 是由重新排列源单词的所有字母得到的一个新单词。
'''
class Solution(object):
    def groupAnagrams(self, strs):
        n = len(strs)
        temp = []
        existDict = {}
        for i in range(n):
            l = list(strs[i])
            temp.append(''.join(sorted(l)))
        groupedIndex = []
        for i in range(n):
            if temp[i] not in existDict.keys():
                groupedIndex.append([])
                groupedIndex[-1].append(i)
                existDict[temp[i]] = len(groupedIndex) - 1
            else:
                groupedIndex[existDict[temp[i]]].append(i)
        res = []
        for group in groupedIndex:
            res.append([])
            for idx in group:
                res[-1].append(strs[idx])
        return res
