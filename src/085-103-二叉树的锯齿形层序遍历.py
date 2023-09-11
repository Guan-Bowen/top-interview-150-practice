'''
给你二叉树的根节点 root ，返回其节点值的 锯齿形层序遍历 。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。
'''
class Solution(object):
    def __init__(self):
        self.depthDict = dict()
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.buildDepthDict(root, 0)
        h = len(self.depthDict)
        res = []
        for i in range(h):
            if i % 2 == 0: res.append(self.depthDict[i])
            else: res.append(reversed(self.depthDict[i]))
        return res
    
    def buildDepthDict(self, node, dp):
        if not node: return
        if dp in self.depthDict: (self.depthDict[dp]).append(node.val)
        else: self.depthDict[dp] = [node.val]
        if node.left: self.buildDepthDict(node.left, dp + 1)
        if node.right: self.buildDepthDict(node.right, dp + 1)