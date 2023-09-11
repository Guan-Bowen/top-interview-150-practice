'''
给你二叉树的根节点 root ，返回其节点值的 层序遍历 。 （即逐层地，从左到右访问所有节点）。
'''
class Solution(object):
    def __init__(self):
        self.depthDict = dict()
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.buildDepthDict(root, 0)
        h = len(self.depthDict)
        res = []
        for i in range(h):
            res.append(self.depthDict[i])
        return res

    def buildDepthDict(self, node, dp):
        if not node: return
        if dp in self.depthDict: (self.depthDict[dp]).append(node.val)
        else: self.depthDict[dp] = [node.val]
        if node.left: self.buildDepthDict(node.left, dp + 1)
        if node.right: self.buildDepthDict(node.right, dp + 1)