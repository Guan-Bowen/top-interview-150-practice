'''
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
'''
class Solution(object):
    def __init__(self):
        self.pathList = []
        self.gotRes = False
    
    def initialize(self):
        self.pathList = []
        self.gotRes = False
    
    def copyPathList(self):
        res = []
        for node in self.pathList:
            res.append(node)
        return res

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.findPath(root, p)
        pathToP = self.copyPathList()
        self.initialize()
        self.findPath(root, q)
        pathToQ = self.copyPathList()
        sizeP, sizeQ= len(pathToP), len(pathToQ)
        size = min(sizeP, sizeQ)
        for i in range(size):
            if pathToP[i] != pathToQ[i]: return pathToP[i - 1]
        return pathToP[size - 1]
        
    
    def findPath(self, node, tar):
        if not node or self.gotRes: return
        self.pathList.append(node)
        if node == tar:
            self.gotRes = True
            return
        self.findPath(node.left, tar)
        self.findPath(node.right, tar)
        if self.gotRes: return
        else: self.pathList.pop()