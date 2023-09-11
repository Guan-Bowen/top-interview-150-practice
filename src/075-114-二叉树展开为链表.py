'''
给你二叉树的根结点 root ，请你将它展开为一个单链表：

展开后的单链表应该同样使用 TreeNode ，其中 right 子指针指向链表中下一个结点，而左子指针始终为 null 。
展开后的单链表应该与二叉树 先序遍历 顺序相同。
'''
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        preOrderList = []
        preOrder(root, preOrderList)
        n = len(preOrderList)
        if n <= 1: return
        for i in range(0, n - 1):
            (preOrderList[i]).left = None
            (preOrderList[i]).right = preOrderList[i + 1]

def preOrder(node, lst):
    if not node: return
    lst.append(node)
    preOrder(node.left, lst)
    preOrder(node.right, lst)