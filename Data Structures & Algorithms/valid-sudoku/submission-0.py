from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        array_two = [False] * 9
        for i in range(0, 9):
            array = [False] * 9
            array_two = [False] * 9
            for j in range(0, 9):
                if (board[j][i] != '.'):
                    if (array_two[int(board[j][i]) - 1] == True):
                        return False
                    else:
                        array_two[int(board[j][i]) - 1] = True
                if (board[i][j] != '.'):
                    if (array[int(board[i][j]) - 1] == True):
                        return False
                    else:
                        array[int(board[i][j]) - 1] = True
        for w in range(0,3):
            for k in range(0,3):
                array_three = [False] * 9
                for i in range(0,3):
                    for j in range(0,3):
                        if (board[i + (k*3)][j + (w*3)] != '.'):
                            if (array_three[int(board[i + (k*3)][j + (w*3)]) - 1] == True):
                                return False
                            else:
                                array_three[int(board[i + (k*3)][j+ (w*3)]) - 1] = True 

        return True

