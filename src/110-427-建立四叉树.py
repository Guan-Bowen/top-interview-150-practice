'''
给你一个 n * n 矩阵 grid ，矩阵由若干 0 和 1 组成。请你用四叉树表示该矩阵 grid 。

你需要返回能表示矩阵 grid 的 四叉树 的根结点。

四叉树数据结构中，每个内部节点只有四个子节点。此外，每个节点都有两个属性：

val：储存叶子结点所代表的区域的值。1 对应 True，0 对应 False。注意，当 isLeaf 为 False 时，你可以把 True 或者 False 赋值给节点，两种值都会被判题机制 接受 。
isLeaf: 当这个节点是一个叶子结点时为 True，如果它有 4 个子节点则为 False 。
class Node {
    public boolean val;
    public boolean isLeaf;
    public Node topLeft;
    public Node topRight;
    public Node bottomLeft;
    public Node bottomRight;
}
'''
"""
# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution(object):
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        n = len(grid)
        def checkConsistance(x, y, a):
            c = grid[x][y]
            for i in range(x, x + a):
                for j in range(y, y + a):
                    if grid[i][j] != c: return False, 0
            return True, c

        def buildTetraTree(x, y, a):
            isLeaf, v = checkConsistance(x, y, a)
            if isLeaf: return Node(val=v, isLeaf=True, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None)
            else:
                node = Node(val=v, isLeaf=False)
                a2 = a // 2
                node.topLeft = buildTetraTree(x, y, a2)
                node.topRight = buildTetraTree(x, y + a2, a2)
                node.bottomLeft = buildTetraTree(x + a2, y, a2)
                node.bottomRight = buildTetraTree(x + a2, y + a2, a2)
                return node
        
        return buildTetraTree(0, 0, n)