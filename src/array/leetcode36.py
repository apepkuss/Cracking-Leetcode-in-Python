
class Solution(object):
    """
    @ Snapchat, Uber, Apple

    Determine if a Sudoku is valid. The Sudoku board could be partially filled, where empty cells are filled
    with the character '.'.

    The rules is here: http://sudoku.com.au/TheRules.aspx
    """

    def isValidSudoku_ThreeIterations(self, board): # n space
        if board is None:
            return False
        m, n = len(board), len(board[0])

        # check if each row meets the rules
        for i in xrange(m):
            tmp = [x for x in board[i] if x != '.']
            if len(tmp) != len(set(tmp)):
                return False

        # check if each column meets the rules
        for j in xrange(n):
            tmp = []
            for i in xrange(m):
                if board[i][j] != '.':
                    tmp.append(board[i][j])
            if len(tmp) != len(set(tmp)):
                return False

        # check if each 3*3-sqaure meets the rules
        for i in xrange(0, m, 3):
            for j in xrange(0, n, 3):
                tmp = board[i][j:j + 3] + board[i + 1][j:j + 3] + board[i + 2][j:j + 3]
                tmp = [x for x in tmp if x != '.']
                if len(tmp) != len(set(tmp)):
                    return False

        return True

    def isValidSudoku_TwoIterations(self, board): # 3 * n space
        if board is None:
            return False
        n = len(board)
        row = set()
        col = set()
        block = set()

        # check each row and column
        for i in range(n):
            row.clear()
            col.clear()
            for j in range(n):
                cell = board[i][j]
                if cell != '.':
                    if cell not in row:
                        row.add(cell)
                    else:
                        return False
                cell = board[j][i]
                if cell != '.':
                    if cell not in col:
                        col.add(cell)
                    else:
                        return False
        # check each block
        for i in range(0, n, 3):
            for j in range(0, n, 3):
                block.clear()
                for u in range(i, i + 3):
                    for v in range(j, j + 3):
                        cell = board[u][v]
                        if cell != '.':
                            if cell not in block:
                                block.add(cell)
                            else:
                                return False
        return True

    def isValidSudoku_OneIteration(self, board): # O(n^2) space
        if board is None:
            return False
        n = len(board)
        rows = [[False] * n for _ in range(n)]
        cols = [[False] * n for _ in range(n)]
        blocks = [[False] * n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if board[i][j] != '.':
                    idx = int(board[i][j]) - 1
                    # check row
                    if rows[i][idx]:
                        return False
                    else:
                        rows[i][idx] = True
                    # check column
                    if cols[j][idx]:
                        return False
                    else:
                        cols[j][idx] = True
                    # check block
                    if blocks[(i/3)*3 + (j/3)][idx]:
                        return False
                    else:
                        blocks[(i/3)*3 + (j/3)][idx] = True
        return True



