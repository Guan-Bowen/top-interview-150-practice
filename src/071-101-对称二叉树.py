'''
给你一个二叉树的根节点 root ， 检查它是否轴对称。
'''
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return check(root.left, root.right)

def check(node1, node2):
    if node1 == None and node2 == None: return True
    elif not (node1 != None and node2 != None): return False
    if node1.val != node2.val: return False
    return check(node1.left, node2.right) and check(node1.right, node2.left)