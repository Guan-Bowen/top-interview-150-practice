'''
二叉树中的 路径 被定义为一条节点序列，序列中每对相邻节点之间都存在一条边。同一个节点在一条路径序列中 至多出现一次 。该路径 至少包含一个 节点，且不一定经过根节点。

路径和 是路径中各节点值的总和。

给你一个二叉树的根节点 root ，返回其 最大路径和 。
'''
class Solution(object):
    def __init__(self):
        self.maxValue = -3e+08
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.calculate(root)
        return self.maxValue

    def calculate(self, node):
        if not node: return 0
        leftValue = self.calculate(node.left)
        rightValue = self.calculate(node.right)
        sumValue = node.val + leftValue + rightValue
        self.maxValue = max(self.maxValue, sumValue)
        return max(0, max(leftValue, rightValue) + node.val)