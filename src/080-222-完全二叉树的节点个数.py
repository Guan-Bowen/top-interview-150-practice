'''
给你一棵 完全二叉树 的根节点 root ，求出该树的节点个数。

完全二叉树 的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，并且最下面一层的节点都集中在该层最左边的若干位置。若最底层为第 h 层，则该层包含 1~ 2h 个节点。
'''
class Solution(object):
    def countNodes(self, root):
        if not root: return 0
        ptr, h = root, -1
        while ptr:
            ptr, h = ptr.left, h + 1
        lo, hi = 2 ** h, 2 ** (h + 1) - 1
        while lo < hi:
            tar = (lo + hi) // 2
            if self.found(h, tar, root): 
                if lo != tar: lo = tar
                else: break
                # print "lo = ", lo, "hi = ", hi, "found: ", tar
            else: 
                hi = tar
                # print "not found: ", tar
        if lo + 1 <= 2 ** (h + 1) - 1 and self.found(h, lo + 1, root): return lo + 1
        else: return lo
    def found(self, h, tar, root):
        ptr = root
        currIdx = 1
        for i in range(h):
            if tar < (currIdx * 2 + 1) * 2 ** (h - 1 - i):  ptr, currIdx = ptr.left, currIdx * 2
            else: ptr, currIdx = ptr.right, currIdx * 2 + 1
        if ptr: return True
        else: return False