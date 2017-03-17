

import heapq

class Solution(object):
    """
    @ Google, Twitter

    Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest
    element in the matrix.

    Note that it is the kth smallest element in the sorted order, not the kth distinct element.

    Example:

        matrix = [
           [ 1,  5,  9],
           [10, 11, 13],
           [12, 13, 15]
        ],
        k = 8,

        return 13.

    Note:
        You may assume k is always valid, 1 <= k <= n2.
    """
    def kthSmallest_heap(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        m, n = len(matrix), len(matrix[0])
        q = [(matrix[0][0], 0, 0)]
        res = None
        for _ in range(k):
            res, i, j = heapq.heappop(q)
            if j == 0 and i + 1 < m:
                heapq.heappush(q, (matrix[i+1][j], i+1, j))
            if j + 1 < n:
                heapq.heappush(q, (matrix[i][j+1], i, j+1))
        return res

    def kthSmallest_BinarySearch(self, matrix, k):
        n = len(matrix)
        x, y = matrix[0][0], matrix[n - 1][n - 1]
        while x < y:
            mid = x + ((y - x) >> 1)
            count = self.search_lower_than_mid(matrix, mid)
            if count < k:
                x = mid + 1
            else:
                y = mid
        return x

    def search_lower_than_mid(self, matrix, num):
        n = len(matrix)
        x, y = n - 1, 0
        count = 0
        while x >= 0 and y < n:
            if matrix[x][y] <= num:
                y += 1
                count += x + 1
            else:
                x -= 1
        return count

if __name__ == "__main__":
    matrix = [[1,5,9,11],[10,11,14,15],[11,12,15,17],[13,14,16,18]]
    k = 8
    res = Solution().kthSmallest_BinarySearch(matrix, k)
    print res

