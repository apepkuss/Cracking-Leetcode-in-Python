
class Solution(object):
    """
    @ Snapchat, Uber, Apple
    
    Hash Table

    Determine if a Sudoku is valid. The Sudoku board could be partially filled, where empty cells are filled
    with the character '.'.

    The rules is here: http://sudoku.com.au/TheRules.aspx
    """

    def isValidSudoku(self, board):
        visited = set()
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    curr = board[i][j]
                    # check if current cell has already appeared in current row, column, and 3*3 grid
                    if (i, curr) in visited or (curr, j) in visited or (i / 3, j / 3, curr) in visited:
                        return False

                    visited.add((i, curr))
                    visited.add((curr, j))
                    visited.add((i / 3, j / 3, curr))
        return True



