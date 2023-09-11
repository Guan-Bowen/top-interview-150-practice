'''
给你两棵二叉树的根节点 p 和 q ，编写一个函数来检验这两棵树是否相同。

如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。
'''
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p == None and q == None: return True
        elif p == None or q == None: return False
        return check(p, q)

def check(n1, n2):
    if n1.val != n2.val: return False
    n1L, n1R, n2L, n2R = n1.left, n1.right, n2.left, n2.right
    if (n1L == None and n2L != None) or (n1L != None and n2L == None): return False
    if (n1R == None and n2R != None) or (n1R != None and n2R == None): return False
    if n1L and n1R: return check(n1L, n2L) and check(n1R, n2R)
    elif n1L: return check(n1L, n2L)
    elif n1R: return check(n1R, n2R)
    else: return True