
class Solution(object):
    """
    @ Amazon, Google, Apple

    Binary Search, Divide and Conquer

    Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

    Integers in each row are sorted in ascending from left to right.
    Integers in each column are sorted in ascending from top to bottom.
    For example,

    Consider the following matrix:

    [
      [1,   4,  7, 11, 15],
      [2,   5,  8, 12, 19],
      [3,   6,  9, 16, 22],
      [10, 13, 14, 17, 24],
      [18, 21, 23, 26, 30]
    ]
    Given target = 5, return true.

    Given target = 20, return false.
    """
    def searchMatrix_iterative(self, matrix, target): # RT: O(m+n)
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m ,n = len(matrix), len(matrix[0])
        y = n-1
        for x in xrange(m):
            while y >= 0 and matrix[x][y] > target:
                y -= 1
            if matrix[x][y] == target:
                return True
        return False

    def searchMatrix_DivideConquer(self, matrix, target):  # RT: O(n^1.58)
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        def helper(matrix, rowStart, rowEnd, colStart, colEnd, target):
            if rowStart > rowEnd or colStart > colEnd:
                return False

            rowMid = (rowStart+rowEnd)/2
            colMid = (colStart+colEnd)/2

            if matrix[rowMid][colMid] > target:
                return helper(matrix, rowStart, rowMid-1, colStart, colMid-1, target) or \
                helper(matrix, rowMid, rowEnd, colStart, colMid-1, target) or \
                helper(matrix, rowStart, rowMid-1, colMid, colEnd, target)

            elif matrix[rowMid][colMid] < target:
                return helper(matrix, rowMid+1, rowEnd, colMid+1, colEnd, target) or \
                helper(matrix, rowMid+1, rowEnd, colStart, colMid, target) or \
                helper(matrix, rowStart, rowMid, colMid+1, colEnd, target)

            else:
                return True

        m, n = len(matrix), len(matrix[0])
        return helper(matrix, 0, m-1, 0, n-1, target)

    def searchMatrix(self, matrix, target):  # RT: O(n^1.58)
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or len(matrix) == 0:
            return False
        m, n = len(matrix), len(matrix[0])
        return self.search(target, matrix, (0, 0), (m - 1, n - 1))

    def search(self, target, matrix, left, right):
        # invalid boundary index
        if left[0] > right[0] or left[1] > right[1]:
            return False

        # base case
        if left == right:
            if matrix[left[0]][left[1]] == target:
                return True
            else:
                return False

        # get mid index
        mid = (left[0] + (right[0] - left[0]) / 2, left[1] + (right[1] - left[1]) / 2)
        value = matrix[mid[0]][mid[1]]
        if target < value:
            return self.search(target, matrix, left, (mid[0] - 1, mid[1] - 1)) or \
                   self.search(target, matrix, (left[0], mid[1]), (mid[0] - 1, right[1])) or \
                   self.search(target, matrix, (mid[0], left[1]), (right[0], mid[1] - 1))
        elif target > value:
            return self.search(target, matrix, (left[0], mid[1] + 1), (mid[0], right[1])) or \
                   self.search(target, matrix, (mid[0] + 1, left[1]), (right[0], mid[1])) or \
                   self.search(target, matrix, (mid[0] + 1, mid[1] + 1), right)
        else:
            return True


if __name__ == "__main__":
    matrix = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
    target = 5
    res = Solution().searchMatrix(matrix, target)
    print res
