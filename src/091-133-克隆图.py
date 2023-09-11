'''
给你无向 连通 图中一个节点的引用，请你返回该图的 深拷贝（克隆）。

图中的每个节点都包含它的值 val（int） 和其邻居的列表（list[Node]）。
'''

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node: return None
        copyDict = dict()
        buildCopyDict(node, copyDict)
        return copyDict[node]


def buildCopyDict(node, copyDict):
    if (not node) or (node in copyDict): return
    if node.neighbors == None: newNode = Node(val=node.val)
    else: newNode = Node(val=node.val, neighbors=[])
    copyDict[node] = newNode
    for n in node.neighbors:
        buildCopyDict(n, copyDict)
        if node.neighbors: (copyDict[node]).neighbors.append(copyDict[n])