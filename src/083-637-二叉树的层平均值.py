'''
给定一个非空二叉树的根节点 root , 以数组的形式返回每一层节点的平均值。与实际答案相差 10-5 以内的答案可以被接受。
'''
class Solution(object):    
    def __init__(self):
        self.depthDict = dict()
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        self.buildDepthDict(root, 0)
        h = len(self.depthDict)
        res = []
        for i in range(h):
            m = len(self.depthDict[i])
            s = sum(self.depthDict[i])
            res.append(s * 1.0 / m)
        return res
    
    def buildDepthDict(self, node, dp):
        if not node: return
        if dp in self.depthDict: (self.depthDict[dp]).append(node.val)
        else: self.depthDict[dp] = [node.val]
        if node.left: self.buildDepthDict(node.left, dp + 1)
        if node.right: self.buildDepthDict(node.right, dp + 1)