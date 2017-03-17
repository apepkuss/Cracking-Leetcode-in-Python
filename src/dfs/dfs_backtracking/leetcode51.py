
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def check(k, y):
            """
            check if the (k+1)-th Queen can be put in column j
            """
            # check the positions of the first k Queens
            for x in xrange(k):
                # the first condition checks if the j-th column is available
                # the second condition checks if the diagonal places are available
                if board[x] == y or abs(k-x) == abs(board[x]-y):
                    return False
            return True

        def dfs(row, valuelist):
            if row == n:
                res.append(valuelist)
            else:
                # iterate n columns
                for col in xrange(n):
                    if check(row, col):
                        board[row] = col
                        s = '.' * n
                        dfs(row+1, valuelist + [s[:col] + 'Q' + s[col+1:]])

        board = [-1 for _ in xrange(n)]
        res = []
        dfs(0, [])
        return res
