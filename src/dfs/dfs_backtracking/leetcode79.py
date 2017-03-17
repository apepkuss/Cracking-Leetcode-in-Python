
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def dfs(x, y, word):
            if len(word ) ==0: return True
            else:
                # up
                if x> 0 and board[x - 1][y] == word[0]:
                    tmp = board[x][y]
                    board[x][y] = '#'
                    if dfs(x - 1, y, word[1:]):
                        return True
                    board[x][y] = tmp

                # down
                if x < len(board) - 1 and board[x + 1][y] == word[0]:
                    tmp = board[x][y]
                    board[x][y] = '#'
                    if dfs(x + 1, y, word[1:]):
                        return True
                    board[x][y] = tmp

                # left
                if y > 0 and board[x][y - 1] == word[0]:
                    tmp = board[x][y]
                    board[x][y] = '#'
                    if dfs(x, y - 1, word[1:]):
                        return True
                    board[x][y] = tmp

                # right
                if y < len(board[0]) - 1 and board[x][y + 1] == word[0]:
                    tmp = board[x][y]
                    board[x][y] = '#'
                    if dfs(x, y + 1, word[1:]):
                        return True
                    board[x][y] = tmp

                return False

        m, n = len(board), len(board[0])
        for x in xrange(m):
            for y in xrange(n):
                # locate the first character of the word in the board
                if board[x][y] == word[0]:
                    if dfs(x, y, word[1:]):
                        return True
        return False


if __name__ == "__main__":
    board = [list("ABCE"),list("SFCS"),list("ADEE")]
    word = "ABCCED"
    res = Solution().exist(board, word)
    print res