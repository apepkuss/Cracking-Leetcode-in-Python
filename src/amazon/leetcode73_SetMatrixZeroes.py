
class Solution(object):
    """
    @ Microsoft, Amazon

    Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.
    """
    def setZeroes_1(self, matrix):    # O(mn) time, O(m+n) space
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m,n = len(matrix), len(matrix[0])
        zerorows = [False for _ in xrange(m)]
        zerocols = [False for _ in xrange(n)]

        for x in xrange(m):
            for y in xrange(n):
                if matrix[x][y] == 0:
                    zerorows[x], zerocols[y] = True, True

        for x in xrange(m):
            for y in xrange(n):
                if zerorows[x] or zerocols[y]:
                    matrix[x][y] = 0

    def setZeroes_2(self, matrix):  # O(m*n) time, O(1) space
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        col0 = False
        for i in range(m):
            if matrix[i][0] == 0: col0 = True
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, 0, -1):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
            if col0: matrix[i][0] = 0