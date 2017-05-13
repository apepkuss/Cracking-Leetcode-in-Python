
class Solution(object):
    """
    @ Amazon
    
    DFS, BFS
    
    Let's play the minesweeper game (Wikipedia, online game)!

    You are given a 2D char matrix representing the game board. 'M' represents an unrevealed mine, 
    'E' represents an unrevealed empty square, 'B' represents a revealed blank square that has no 
    adjacent (above, below, left, right, and all 4 diagonals) mines, digit ('1' to '8') represents 
    how many mines are adjacent to this revealed square, and finally 'X' represents a revealed mine.
    
    Now given the next click position (row and column indices) among all the unrevealed squares ('M' 
    or 'E'), return the board after revealing this position according to the following rules:
    
    If a mine ('M') is revealed, then the game is over - change it to 'X'.
    If an empty square ('E') with no adjacent mines is revealed, then change it to revealed blank ('B') 
    and all of its adjacent unrevealed squares should be revealed recursively.
    If an empty square ('E') with at least one adjacent mine is revealed, then change it to a digit ('1' 
    to '8') representing the number of adjacent mines.
    
    Return the board when no more squares will be revealed.
    
    Note:
    The range of the input matrix's height and width is [1,50].
    
    The click position will only be an unrevealed square ('M' or 'E'), which also means the input board 
    contains at least one clickable square.
    
    The input board won't be a stage when game is over (some mines have been revealed).
    
    For simplicity, not mentioned rules should be ignored in this problem. For example, you don't need to 
    reveal all the unrevealed mines when the game is over, consider any cases that you will win the game or 
    flag any squares.
    """
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        click = tuple(click)
        stack = [click]
        seen = set()
        while stack:
            c = stack.pop()
            seen.add(c)
            i, j = c[0], c[1]
            # Rule 1
            if board[i][j] == 'M':
                board[i][j] = 'X'
                break
            else:
                # count adjacent mines
                mines = sum(board[nr][nc ] =='M' for nr, nc in self.neighbors(board, i, j))
                if mines:
                    # Rule 3
                    board[i][j] = str(mines)
                else:
                    # Rule 2
                    board[i][j] = 'B'
                    for nei in self.neighbors(board, i, j):
                        if board[nei[0]][nei[1]] in 'ME' and nei not in seen:
                            stack.append(nei)
        return board

    def neighbors(self, board, i, j):
        m, n = len(board), len(board[0])
        for dr in range(-1, 2):
            for dc in range(-1, 2):
                if (dr or dc) and 0<= dr + i < m and 0 <= dc + j < n:
                    yield dr + i, dc + j



