
class Solution(object):
    """
    @ Dropbox, Google, Two Sigma, Snapchat

    Array

    Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with
    its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above
    Wikipedia article):

    1. Any live cell with fewer than two live neighbors dies, as if caused by under-population.
    2. Any live cell with two or three live neighbors lives on to the next generation.
    3. Any live cell with more than three live neighbors dies, as if by over-population..
    4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

    Write a function to compute the next state (after one update) of the board given its current state.

    Follow up:
    1. Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot
       update some cells first and then use their updated values to update other cells.
    2. In this question, we represent the board using a 2D array. In principle, the board is infinite, which
       would cause problems when the active area encroaches the border of the array. How would you address these
       problems?
    """

    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        def live_neighbors(board, i, j):
            """compute the number of live neighbors of cell[i][j]"""
            m, n = len(board), len(board[0])
            lives = 0

            # traverse eight neighbors of cell[i][j]
            for x in range(max(i - 1, 0), min(i + 1, m - 1) + 1):
                for y in range(max(j - 1, 0), min(j + 1, n - 1) + 1):
                    lives += board[x][y] & 1

            # remove board[i][j] from lives
            lives -= board[i][j] & 1

            return lives

        if board is None or len(board) == 0:
            return
        m, n = len(board), len(board[0])

        # for each cell, [first bit is original value] => [second bit is next value, first bit is original value]
        for i in range(m):
            for j in range(n):
                # count the number of live neighbors of board[i][j]
                lives = live_neighbors(board, i, j)

                if board[i][j] == 1 and (2 <= lives <= 3):
                    # rule 2
                    board[i][j] = 3  # from 0x01 -> 0x11

                elif board[i][j] == 0 and lives == 3:
                    # rule 4
                    board[i][j] = 2  # from 0x00 -> 0x10

        # right shift the value of each cell to get next state
        for i in range(m):
            for j in range(n):
                board[i][j] >>= 1

