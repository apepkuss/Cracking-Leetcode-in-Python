
class Solution(object):
    """
    @ Amazon, Microsoft, Google, Facebook, Zenefits
    
    Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded
    by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four
    edges of the grid are all surrounded by water.
    """
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def dfs(x, y):
            grid[x][y] = '*'
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                xx, yy = x+dx, y+dy
                if 0<=xx<len(grid) and 0<=yy<len(grid[0]) and grid[xx][yy] == '1':
                    dfs(xx, yy)
            
        m, n = len(grid), len(grid[0])
        islands = 0
        for x in xrange(m):
            for y in xrange(n):
                if grid[x][y] == '1':
                    dfs(x, y)
                    islands += 1
        return islands

if __name__ == "__main__":
    grid = [list("11110"), list("11010"), list("11000"), list("00000")]
    res = Solution().numIslands(grid)
    print res
