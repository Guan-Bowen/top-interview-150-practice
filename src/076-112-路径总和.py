'''
给你二叉树的根节点 root 和一个表示目标和的整数 targetSum 。判断该树中是否存在 根节点到叶子节点 的路径，这条路径上所有节点值相加等于目标和 targetSum 。如果存在，返回 true ；否则，返回 false 。

叶子节点 是指没有子节点的节点。
'''
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if not root: return False
        return judge(root, targetSum)

def judge(node, tar):
    if not node: return False
    tar -= node.val
    if not node.left and not node.right:
        if tar == 0: return True
        else: return False
    else:
        return judge(node.left, tar) or judge(node.right, tar)