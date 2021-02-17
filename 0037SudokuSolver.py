"""
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.



Example 1:


Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
Explanation: The input board is shown above and the only valid solution is shown below:




Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit or '.'.
It is guaranteed that the input board has only one solution.
"""

class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        i = 0
        j = 0
        while i < 9:
            while j < 9:
                if board[i][j] != '.':
                    j += 1
                else:
                    break
            if j < 9 and i < 9 and board[i][j] == '.':
                break
            i += 1
            j = 0
        if i == 9:
            return board
        return self.check(board, i, j)[1]

    def check(self, board, i, j):
        right = 0
        i0 = i
        j0 = j
        for k in range(1, 10):
            i = i0
            j = j0
            if self.right(board, i, j, k):
                boardnow = board[::]
                boardnow[i] = boardnow[i][::]
                boardnow[i][j] = str(k)
                while i < 9:
                    while j < 9:
                        if boardnow[i][j] != '.':
                            j += 1
                        else:
                            break
                    if j < 9 and i < 9 and board[i][j] == '.':
                        break
                    i += 1
                    j = 0
                if i == 9:
                    return [1, boardnow]
                result = self.check(boardnow, i, j)
                if result[0]:
                    return result
        return [0, 0]

    def right(self, board, i, j, k):
        k = str(k)
        if k in board[i]:
            return False
        for m in range(9):
            if board[m][j] == k:
                return False
        x = i // 3
        y = j // 3
        for m in range(3):
            for n in range(3):
                if board[3 * x + m][3 * y + n] == k:
                    return False
        return True