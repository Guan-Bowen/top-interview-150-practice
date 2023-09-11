'''
给你一个二叉搜索树的根节点 root ，返回 树中任意两不同节点值之间的最小差值 。

差值是一个正数，其数值等于两值之差的绝对值。
'''
class Solution(object):
    def __init__(self):
        self.inOrderList = []

    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.inOrder(root)
        n = len(self.inOrderList)
        res = 100000
        for i in range(n - 1):
            res = min(res, self.inOrderList[i + 1] - self.inOrderList[i])
        return res
    
    def inOrder(self, node):
        if not node: return
        self.inOrder(node.left)
        self.inOrderList.append(node.val)
        self.inOrder(node.right)