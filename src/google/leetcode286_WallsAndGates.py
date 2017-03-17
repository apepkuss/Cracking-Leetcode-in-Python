

class Solution(object):
    """
    @ Google, Facebook

    You are given a m x n 2D grid initialized with these three possible values.

    -1 - A wall or an obstacle.
    0 - A gate.
    INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
    Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

    For example, given the 2D grid:
    INF  -1  0  INF
    INF INF INF  -1
    INF  -1 INF  -1
      0  -1 INF INF
    After running your function, the 2D grid should be:
      3  -1   0   1
      2   2   1  -1
      1  -1   2  -1
      0  -1   3   4
    """

    def wallsAndGates_dfs(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """

        def dfs(i, j):
            for x, y in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):
                if 0 <= x < m and 0 <= y < n and rooms[x][y] > rooms[i][j] + 1:
                    rooms[x][y] = rooms[i][j] + 1
                    dfs(x, y)

        if rooms is None or rooms == []:
            return
        m, n = len(rooms), len(rooms[0])
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    dfs(i, j)

    def wallsAndGates_bfs(self, rooms):
        if rooms is None or rooms == []:
            return
        m, n = len(rooms), len(rooms[0])
        queue = []
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    queue.append((i, j))
        INF = 2147483647
        while len(queue) > 0:
            i, j = queue.pop(0)
            for x, y in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):
                if 0 <= x < m and 0 <= y < n and rooms[x][y] == INF:
                    rooms[x][y] = rooms[i][j] + 1
                    queue.append((x, y))