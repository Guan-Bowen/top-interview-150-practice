'''
给你一个大小为 n x n 的整数矩阵 board ，方格按从 1 到 n2 编号，编号遵循 转行交替方式 ，从左下角开始 （即，从 board[n - 1][0] 开始）每一行交替方向。

玩家从棋盘上的方格 1 （总是在最后一行、第一列）开始出发。

每一回合，玩家需要从当前方格 curr 开始出发，按下述要求前进：

选定目标方格 next ，目标方格的编号符合范围 [curr + 1, min(curr + 6, n2)] 。
该选择模拟了掷 六面体骰子 的情景，无论棋盘大小如何，玩家最多只能有 6 个目的地。
传送玩家：如果目标方格 next 处存在蛇或梯子，那么玩家会传送到蛇或梯子的目的地。否则，玩家传送到目标方格 next 。 
当玩家到达编号 n2 的方格时，游戏结束。
r 行 c 列的棋盘，按前述方法编号，棋盘格中可能存在 “蛇” 或 “梯子”；如果 board[r][c] != -1，那个蛇或梯子的目的地将会是 board[r][c]。编号为 1 和 n2 的方格上没有蛇或梯子。

注意，玩家在每回合的前进过程中最多只能爬过蛇或梯子一次：就算目的地是另一条蛇或梯子的起点，玩家也 不能 继续移动。

举个例子，假设棋盘是 [[-1,4],[-1,3]] ，第一次移动，玩家的目标方格是 2 。那么这个玩家将会顺着梯子到达方格 3 ，但 不能 顺着方格 3 上的梯子前往方格 4 。
返回达到编号为 n2 的方格所需的最少移动次数，如果不可能，则返回 -1。
'''
class Solution(object):
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        n = len(board)
        cache = [0] * (n ** 2)
        idx = 0
        # 按照奇偶行将地图 “拉” 成一维数组
        # 从最后一行，第一列的元素开始
        for i in range(n - 1, -1, -1):
            if (i - n + 1) % 2: # 奇数行，向左遍历，反向循环
                for j in range(n - 1, -1, -1):
                    cache[idx] = board[i][j]
                    idx += 1            
            else:
                for j in range(n): # 偶数行，向右遍历，正向循环
                    cache[idx] = board[i][j]
                    idx += 1
        q = deque() # 存储 BFS 将要达到的位置
        reached = set() # 排除已经达到的位置
        q.append(0) 
        reached.add(0)
        res = 0
        while q: # BFS
            for _ in range(len(q)): # 第 r 轮的节点逐个出队，将下一轮可达的节点入队
                currentPos = q.popleft()
                if currentPos == n ** 2 - 1: return res
                for i in range(1, 7):
                    nextPos = currentPos + i
                    if nextPos >= n ** 2: break # 不能超过范围
                    if cache[nextPos] != -1: # 发生跳跃，修改目的地
                        nextPos = cache[nextPos] - 1 # 直接跳跃：原来的目的地并未到达
                    if nextPos not in reached:
                        q.append(nextPos)
                        reached.add(nextPos)
            res += 1
        return -1