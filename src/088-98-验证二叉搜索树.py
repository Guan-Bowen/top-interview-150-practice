'''
给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。

有效 二叉搜索树定义如下：

节点的左子树只包含 小于 当前节点的数。
节点的右子树只包含 大于 当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
'''
class Solution(object):
    def __init__(self):
        self.inOrderList = []

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.inOrder(root)
        n = len(self.inOrderList)
        for i in range(n - 1):
            if self.inOrderList[i] >= self.inOrderList[i + 1]: return False
        return True

    def inOrder(self, node):
        if not node: return
        self.inOrder(node.left)
        self.inOrderList.append(node.val)
        self.inOrder(node.right)