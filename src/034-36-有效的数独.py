'''
请你判断一个 9 x 9 的数独是否有效。只需要 根据以下规则 ，验证已经填入的数字是否有效即可。

数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。（请参考示例图）
 

注意：

一个有效的数独（部分已被填充）不一定是可解的。
只需要根据以上规则，验证已经填入的数字是否有效即可。
空白格用 '.' 表示。
'''

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        for i in range(9):
            setRow = set()
            setCol = set()
            for j in range(9):
                bij = board[i][j]
                bji = board[j][i]
                if bij != '.':
                    if bij in setRow: return False
                    else: setRow.add(bij)
                if bji != '.':
                    if bji in setCol: return False
                    else: setCol.add(bji)

            for i in range(3):
                for j in range(3):
                    setSquare = set()
                    for p in range(3):
                        for q in range(3):
                            bx = board[3 * i + p][3 * j + q]
                            if bx != '.':
                                if bx in setSquare: return False
                                else: setSquare.add(bx)
            
            return True
