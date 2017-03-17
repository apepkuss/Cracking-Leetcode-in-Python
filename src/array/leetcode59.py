
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 0: return []
        matrix = [[0 for i in range(n)] for j in range(n)]
        top = 0; bottom = len(matrix)-1
        left = 0; right = len(matrix[0])-1
        direct = 0; count = 0
        while True:
            if direct == 0:
                for i in range(left, right+1):
                    count += 1; matrix[top][i] = count
                top += 1
            elif direct == 1:
                for i in range(top, bottom+1):
                    count += 1; matrix[i][right] = count
                right -= 1
            elif direct == 2:
                for i in range(right, left-1, -1):
                    count += 1; matrix[bottom][i] = count
                bottom -= 1
            elif direct == 3:
                for i in range(bottom, top-1, -1):
                    count += 1; matrix[i][left] = count
                left += 1
            if count == n*n: return matrix
            direct = (direct+1) % 4
