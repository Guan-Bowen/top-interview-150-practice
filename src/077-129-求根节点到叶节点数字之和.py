'''
给你一个二叉树的根节点 root ，树中每个节点都存放有一个 0 到 9 之间的数字。
每条从根节点到叶节点的路径都代表一个数字：

例如，从根节点到叶节点的路径 1 -> 2 -> 3 表示数字 123 。
计算从根节点到叶节点生成的 所有数字之和 。

叶节点 是指没有子节点的节点。
'''
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        resList = []
        stat(root, resList, '')
        return sum(resList)

def stat(node, resList, subString):
    if not node: return
    newSubString = subString + str(node.val)
    if not node.left and not node.right:
        resList.append(int(newSubString))
    else:
        stat(node.left, resList, newSubString)
        stat(node.right, resList, newSubString)