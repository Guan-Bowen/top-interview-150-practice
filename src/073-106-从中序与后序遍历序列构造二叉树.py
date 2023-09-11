'''
给定两个整数数组 inorder 和 postorder ，其中 inorder 是二叉树的中序遍历， postorder 是同一棵树的后序遍历，请你构造并返回这颗 二叉树 。
'''
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        postorder.reverse()
        return build(postorder, inorder)

def build(rrlPo, io):
    lenP, lenI = len(rrlPo), len(io)
    if lenI == 0: return None
    key = rrlPo[0]
    rrlPo.pop(0)
    splitIndex = io.index(key)
    newNode = TreeNode(val=key)
    subLeftIo = io[:splitIndex]
    subRightIo = io[splitIndex + 1:]
    newNode.right = build(rrlPo, subRightIo)
    newNode.left = build(rrlPo, subLeftIo)
    return newNode