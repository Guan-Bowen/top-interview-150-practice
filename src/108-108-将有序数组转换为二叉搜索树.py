'''
给你一个整数数组 nums ，其中元素已经按 升序 排列，请你将其转换为一棵 高度平衡 二叉搜索树。

高度平衡 二叉树是一棵满足「每个节点的左右两个子树的高度差的绝对值不超过 1 」的二叉树。
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return buildBiTree(nums)

def buildBiTree(numList):
    sz = len(numList)
    if not sz: return
    rootIndex = sz // 2
    newNode = TreeNode(val=numList[rootIndex])
    newNode.left = buildBiTree(numList[:rootIndex])
    newNode.right = buildBiTree(numList[rootIndex + 1:])
    return newNode