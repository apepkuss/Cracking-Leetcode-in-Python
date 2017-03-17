

class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        if matrix == []:
            return
        self.m = len(matrix); self.n = len(matrix[0])
        self.accumulate = [[0 for _ in range(self.n)] for _ in range(self.m)]
        for i in range(self.m):
            for j in range(self.n):
                self.accumulate[i][j] = self.accumulate[i][j-1] + matrix[i][j]

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if row1>row2 or col1>col2 or row1<0 or row2>=self.m or col1<0 or col2>=self.n:
            return 0
        result = 0
        for i in range(row1, row2+1):
            if col1 == 0:
                result += self.accumulate[i][col2]
            else:
                result += self.accumulate[i][col2] - self.accumulate[i][col1-1]
        return result
