
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

    def setZeroes_2(self, matrix, verbose=False):  # O(m*n) time, O(1) space
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # To optimaize the space complexity, store states of each row in the first of that row, and store states
        # of each column in the first of that column. Because the state of row0 and the state of column0 would
        # occupy the same cell, I let it be the state of row0, and use another variable "col0" for column0. In
        # the first phase, use matrix elements to set states in a top-down way. In the second phase, use states
        # to set matrix elements in a bottom-up way.

        m, n = len(matrix), len(matrix[0])

        # store the state of column0
        col0 = False

        # use matrix elements to set states in a top-down way
        for i in range(m):
            if matrix[i][0] == 0:
                col0 = True

            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0

            if verbose:
                print('After scan row {0}'.format(i))
                print('row {0}: {1}'.format(i, matrix[i]))
                print('row {0}: {1}'.format(0, matrix[0]))

        # use states to set matrix elements in a bottom-up way
        for i in range(m - 1, -1, -1):
            # set the last n-1 columns from 2 to n
            for j in range(n - 1, 0, -1):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

            # set the first column of each row
            if col0:
                matrix[i][0] = 0

            if verbose:
                print('row {0}: {1}'.format(i, matrix[i]))
