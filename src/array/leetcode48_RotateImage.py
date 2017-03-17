
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
        rows = len(matrix)
        cols = len(matrix[0])

        if rows<2 or cols<2:
            return

        # invert the matrix
        for j in range(cols):
            for i in range(rows/2):
                matrix[i][j], matrix[rows-1-i][j] = matrix[rows-1-i][j], matrix[i][j]

        # flap the matrix along the main diagonal
        for i in range(rows):
            for j in range(i+1,cols):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
