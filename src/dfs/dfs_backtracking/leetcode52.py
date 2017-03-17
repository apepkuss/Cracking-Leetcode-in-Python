
class Solution(object):
    def totalNQueens(self, n): # recursion+backtracking
        """
        :type n: int
        :rtype: int
        """
        def check(k, j):
            for i in xrange(k):
                if board[i] == j or abs(i-k) == abs(board[i]-j):
                    return False
            return True

        def dfs(depth):
            if depth == n:
                self.count += 1
            else:
                for i in xrange(n):
                    if check(depth, i):
                        board[depth] = i
                        dfs(depth+1)

        self.count = 0
        board = [0 for _ in xrange(n)]
        dfs(0)
        return self.count
