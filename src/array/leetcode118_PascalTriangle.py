
class Solution(object):
    """
    @ Apple, Twitter
    
    Given numRows, generate the first numRows of Pascal's triangle.

    For example, given numRows = 5,
    Return
    
    [
         [1],
        [1,1],
       [1,2,1],
      [1,3,3,1],
     [1,4,6,4,1]
    ]
    """

    def generate_iterative(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []

        if numRows == 0:
            return res

        for row in range(numRows):
            column = []
            for col in range(numRows):
                if col == 0 or col == row:
                    column.append(1)
                if 0 < col < row:
                    column.append(res[row - 1][col - 1] + res[row - 1][col])
            res.append(column)

        return res

    def generate_dfs(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        if numRows == 0:
            return res

        return self.dfs([1], 1, numRows, res)

    def dfs(self, curr, k, n, res):
        res.append(curr)

        if k == n:
            return res

        # build up next row
        next_row = [1]
        for i in range(1, k):
            next_row.append(curr[i-1] + curr[i])
        next_row.append(1)

        return self.dfs(next_row, k+1, n, res)


if __name__ == "__main__":
    res = Solution().generate_dfs(3)
    print res

