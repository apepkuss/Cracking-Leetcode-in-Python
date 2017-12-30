
class Solution(object):
    """
    @ Amazon, Microsoft, Apple

    Array

    You are given an n x n 2D matrix representing an image.

    Rotate the image by 90 degrees (clockwise).

    Follow up: Could you do this in-place?
    """
    def rotate(self, matrix):   # O(n^2) time
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        assert matrix is not None

        rows = len(matrix)
        cols = len(matrix[0])

        if rows < 2 or cols < 2:
            return

        print('Before rotate: {0}'.format(matrix))

        # invert the matrix
        i, j = 0, rows-1
        while i < j:
            matrix[i], matrix[j] = matrix[j], matrix[i]
        print('After invert: {0}'.format(matrix))

        # flap the matrix along the main diagonal
        for i in range(rows):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        print('After flap: {0}'.format(matrix))
