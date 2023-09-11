'''
给你一棵二叉树的根节点 root ，翻转这棵二叉树，并返回其根节点。
'''
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        wrap(root)
        return root

def wrap(node):
    if node == None: return
    nL, nR = node.left, node.right
    wrap(nL)
    wrap(nR)
    node.left, node.right = node.right, node.left