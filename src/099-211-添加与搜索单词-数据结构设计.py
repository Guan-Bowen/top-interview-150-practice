'''
请你设计一个数据结构，支持 添加新单词 和 查找字符串是否与任何先前添加的字符串匹配 。

实现词典类 WordDictionary ：

WordDictionary() 初始化词典对象
void addWord(word) 将 word 添加到数据结构中，之后可以对它进行匹配
bool search(word) 如果数据结构中存在字符串与 word 匹配，则返回 true ；否则，返回  false 。word 中可能包含一些 '.' ，每个 . 都可以表示任何一个字母。
'''
class Trie(object):
    def __init__(self):
        self.child = dict()
        self.isWord = False

class WordDictionary(object):

    def __init__(self):
        self.root = Trie()

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        curr = self.root
        for char in word:
            if char not in curr.child: curr.child[char] = Trie()
            curr = curr.child[char]
        curr.isWord = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        def dfs(node, start, word):
            sz = len(word)
            if start == sz: return node.isWord
            for i in range(start, sz):
                if word[i] != '.':
                    if word[i] not in node.child: return False
                    return dfs(node.child[word[i]], i + 1, word)
                else:
                    if not node.child: return False
                    res = False
                    for key in node.child:
                        res = res or dfs(node.child[key], i + 1, word)
                        if res: break
                    return res
        return dfs(self.root, 0, word)




# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)