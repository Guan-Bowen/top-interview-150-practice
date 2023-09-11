'''
给定一个二叉树：

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL 。

初始状态下，所有 next 指针都被设置为 NULL 。
'''
class Solution(object):
    def __init__(self):
        self.depthDict = {}
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root: return None
        self.buildDepthDict(root, 1)
        i = 1
        while i in self.depthDict:
            l = len(self.depthDict[i])
            if l > 1:
                for j in range(0, l - 1): (self.depthDict[i][j]).next = (self.depthDict[i][j + 1])
            i += 1
        return root


    def buildDepthDict(self, node, depth):
        if not node: return
        # In Order
        if node.left: self.buildDepthDict(node.left, depth + 1)
        if depth not in self.depthDict: self.depthDict[depth] = [node]
        else: (self.depthDict[depth]).append(node)
        if node.right: self.buildDepthDict(node.right, depth + 1)