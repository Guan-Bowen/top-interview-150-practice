'''
给定两个整数数组 preorder 和 inorder ，其中 preorder 是二叉树的先序遍历， inorder 是同一棵树的中序遍历，请构造二叉树并返回其根节点。
'''
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        return build(preorder, inorder)

def build(po, io):
    lenP, lenI = len(po), len(io)
    if lenI == 0: return None
    key = po[0]
    splitIndex = io.index(key)
    po.pop(0)
    newNode = TreeNode(val=key)
    subLeftIo = io[:splitIndex]
    subRightIo = io[splitIndex + 1:]
    newNode.left = build(po, subLeftIo)
    newNode.right = build(po, subRightIo)
    return newNode