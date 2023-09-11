'''
Trie（发音类似 "try"）或者说 前缀树 是一种树形数据结构，用于高效地存储和检索字符串数据集中的键。这一数据结构有相当多的应用情景，例如自动补完和拼写检查。

请你实现 Trie 类：

Trie() 初始化前缀树对象。
void insert(String word) 向前缀树中插入字符串 word 。
boolean search(String word) 如果字符串 word 在前缀树中，返回 true（即，在检索之前已经插入）；否则，返回 false 。
boolean startsWith(String prefix) 如果之前已经插入的字符串 word 的前缀之一为 prefix ，返回 true ；否则，返回 false 。
'''
class Trie(object):

    def __init__(self):
        self.isWord = False
        self.child = dict()

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        this = self
        for char in word:
            if char not in this.child:
                this.child[char] = Trie()
            this = this.child[char]
        this.isWord = True


    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        this = self
        for char in word:
            if char not in this.child: return False
            this = this.child[char]
        return this.isWord


    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        this = self
        for char in prefix:
            if char not in this.child: return False
            this = this.child[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)