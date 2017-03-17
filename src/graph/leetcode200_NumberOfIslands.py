
class Solution(object):
    """
    @ Amazon, Microsoft, Google, Facebook, Zenefits
    
    Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded
    by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four
    edges of the grid are all surrounded by water.
    """

    # Method 1: use dfs to traverse all paths
    def numIslands_dfs(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        def dfs(x, y):
            grid[x][y] = '*'
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                xx, yy = x + dx, y + dy
                if 0 <= xx < len(grid) and 0 <= yy < len(grid[0]) and grid[xx][yy] == '1':
                    dfs(xx, yy)

        islands = 0
        if grid is None or len(grid) == 0:
            return islands

        m, n = len(grid), len(grid[0])
        for x in xrange(m):
            for y in xrange(n):
                if grid[x][y] == '1':
                    dfs(x, y)
                    islands += 1
        return islands


    # use union-find approach
    def numIslands_UnionFind(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if grid is None or len(grid) == 0:
            return 0

        m, n = len(grid), len(grid[0])
        trees = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    trees += 1

        parent = [i for i in range(m * n)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0':
                    continue

                # index of the parent of grid[i][j]
                p = i * n + j

                # check top neighbor cell
                if i > 0 and grid[i - 1][j] == '1':
                    # q = (i-1) * n + j
                    q = p - n
                    if self.union(p, q, parent):
                        trees -= 1

                # check bottom neighbor cell
                if i < m - 1 and grid[i + 1][j] == '1':
                    # q = (i+1) * n + j
                    q = p + n
                    if self.union(p, q, parent):
                        trees -= 1

                # check left neighbor cell
                if j > 0 and grid[i][j - 1] == '1':
                    q = p - 1
                    if self.union(p, q, parent):
                        trees -= 1

                # check right neighbor cell
                if j < n - 1 and grid[i][j + 1] == '1':
                    q = p + 1
                    if self.union(p, q, parent):
                        trees -= 1

        return trees

    def union(self, p, q, parent):
        """Merge p and q into the same tree"""
        p_root = self.find(p, parent)
        q_root = self.find(q, parent)

        # if p_root == q_root, it means p and q are in the same tree
        # otherwise, p and q should be merged into the same tree
        if p_root == q_root:
            return False

        parent[p_root] = parent[q_root]
        return True

    def find(self, p, parent):
        """Find the ancestor of p"""
        if parent[p] != parent[parent[p]]:
            parent[p] = self.find(parent[p], parent)
        return parent[p]

if __name__ == "__main__":
    grid = [list("11110"), list("11010"), list("11000"), list("00000")]
    res = Solution().numIslands_UnionFind(grid)
    print res
