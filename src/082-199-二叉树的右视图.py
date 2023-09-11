'''
给定一个二叉树的 根节点 root，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。
'''
class Solution(object):
    def __init__(self):
        self.depthDict = dict()
        
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.buildDepthDict(root, 0)
        h = len(self.depthDict)
        res = []
        for i in range(h):
            res.append(self.depthDict[i][-1])
        return res
    
    def buildDepthDict(self, node, dp):
        if not node: return
        if dp in self.depthDict: (self.depthDict[dp]).append(node.val)
        else: self.depthDict[dp] = [node.val]
        if node.left: self.buildDepthDict(node.left, dp + 1)
        if node.right: self.buildDepthDict(node.right, dp + 1)