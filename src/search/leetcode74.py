
class Solution(object):
    def searchMatrix_BS1(self, matrix, target): # RT: O(log(m)+log(n))
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m ,n = len(matrix) ,len(matrix[0])

        # do binary search on the first column
        left , right =0 , m -1
        while left<= right:
            mid = (left + right) / 2
            if target > matrix[mid][0]:
                left = mid + 1
            elif target < matrix[mid][0]:
                right = mid - 1
            else:
                return True
        # do binary search on the index-th row
        index = left - 1
        left = 0
        right = n - 1
        while left <= right:
            mid = (left + right) / 2
            if target > matrix[index][mid]:
                left = mid + 1
            elif target < matrix[index][mid]:
                right = mid - 1
            else:
                return True
        return False

    def searchMatrix_BS2(self, matrix, target):  # RT: O(log(m*n))
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m, n = len(matrix), len(matrix[0])
        start, end = 0, m * n - 1
        while start <= end:
            mid = (start + end) / 2
            # position = row*n+col
            row, col = mid / n, mid % n
            if matrix[row][col] < target:
                start = mid + 1
            elif matrix[row][col] > target:
                end = mid - 1
            else:
                return True
        return False


if __name__ == "__main__":
    matrix = [[1,2,3,4],
              [5,6,7,8],
              [9,10,11,12],
              [13,14,15,16],
              [17,18,19,20],
              [21,22,23,24],
              [25,30,34,50]]
    target = 11
    res = Solution().searchMatrix_BS1(matrix, target)
    print res