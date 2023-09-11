'''
给定一个二叉搜索树的根节点 root ，和一个整数 k ，请你设计一个算法查找其中第 k 个最小元素（从 1 开始计数）。
'''

class Solution(object):
    def __init__(self):
        self.inOrderList = []


    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.inOrder(root)
        return self.inOrderList[k - 1]

    def inOrder(self, node):
        if not node: return
        self.inOrder(node.left)
        self.inOrderList.append(node.val)
        self.inOrder(node.right)