class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowlist = [[0] * 9 for _ in range(9)]
        collist = [[0] * 9 for _ in range(9)]
        sblist = [[0] * 9 for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    num = int(board[i][j]) - 1
                    if rowlist[i][num] or collist[j][num] or sblist[j//3 + (i//3)*3][num]:
                        return False
                    rowlist[i][num] += 1
                    collist[j][num] += 1
                    sblist[(i//3)*3 + j//3][num] += 1
        return True