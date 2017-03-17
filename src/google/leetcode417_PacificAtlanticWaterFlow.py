
class Solution(object):
    """
    @ Google

    Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent,
    the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right
    and bottom edges.

    Water can only flow in four directions (up, down, left, or right) from a cell to another one with height
    equal or lower.

    Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.

    Note:
    The order of returned grid coordinates does not matter.
    Both m and n are less than 150.
    Example:

    Given the following 5x5 matrix:

      Pacific ~   ~   ~   ~   ~
           ~  1   2   2   3  (5) *
           ~  3   2   3  (4) (4) *
           ~  2   4  (5)  3   1  *
           ~ (6) (7)  1   4   5  *
           ~ (5)  1   1   2   4  *
              *   *   *   *   * Atlantic

    Return:

    [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).
    """
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        def dfs(visited, x, y, m, n):
            visited[x][y] = True
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx <= m- 1 and 0 <= ny <= n - 1:
                    if not visited[nx][ny] and matrix[nx][ny] >= matrix[x][y]:
                        dfs(visited, nx, ny, m, n)

        res = []
        m = len(matrix)
        if m == 0: return res
        n = len(matrix[0])
        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0, 0]
        pac = [[False] * n for _ in range(m)]
        atl = [[False] * n for _ in range(m)]
        for i in range(m):
            # left edge
            dfs(pac, i, 0, m, n)
            # right edge
            dfs(atl, i, n - 1, m, n)
        for j in range(n):
            # top edge
            dfs(pac, 0, j, m, n)
            # bottom edge
            dfs(atl, m - 1, j, m, n)
        for i in range(m):
            for j in range(n):
                if pac[i][j] and atl[i][j]:
                    res.append([i, j])
        return res


if __name__ == "__main__":
    matrix = [[1,1],[1,1],[1,1]]
    res = Solution().pacificAtlantic(matrix)
    print res



