'''
字典 wordList 中从单词 beginWord 和 endWord 的 转换序列 是一个按下述规格形成的序列 beginWord -> s1 -> s2 -> ... -> sk：

每一对相邻的单词只差一个字母。
 对于 1 <= i <= k 时，每个 si 都在 wordList 中。注意， beginWord 不需要在 wordList 中。
sk == endWord
给你两个单词 beginWord 和 endWord 和一个字典 wordList ，返回 从 beginWord 到 endWord 的 最短转换序列 中的 单词数目 。如果不存在这样的转换序列，返回 0 。
'''
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordList = set(wordList) # 不用空间换时间会 Timeout
        if endWord not in wordList: return 0
        if beginWord in wordList: wordList.remove(beginWord)
        alphaSet = set()
        for word in wordList:
            for al in word:
                if al not in alphaSet: alphaSet.add(al)
        res = 1
        q = deque()
        q.append(beginWord)
        while q:
            for _ in range(len(q)):
                currentWord = q.popleft()
                if currentWord == endWord: return res
                for j in range(len(currentWord)):
                    for al in alphaSet:
                        temp = currentWord[:j] + al + currentWord[j + 1:]
                        if temp in wordList:
                            q.append(temp)
                            wordList.remove(temp)
            res += 1
        return 0