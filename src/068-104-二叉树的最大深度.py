'''
给定一个二叉树 root ，返回其最大深度。

二叉树的 最大深度 是指从根节点到最远叶子节点的最长路径上的节点数。
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.maxDp = 0
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.f(root, 0)

    def f(self, node, currentDepth):
        if node == None: 
            self.maxDp = max(self.maxDp, currentDepth)
            return currentDepth
        nL, nR = node.left, node.right
        return max(self.f(nL, currentDepth +1), self.f(nR, currentDepth + 1))