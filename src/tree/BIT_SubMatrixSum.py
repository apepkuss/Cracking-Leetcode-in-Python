

class SubMatrixSum(object):

    @classmethod
    def construct_2DBIT(cls, matrix):
        m, n = len(matrix), len(matrix[0])

        BIT = [[0]*(n+1) for _ in xrange(m+1)]

        for x in xrange(1, n+1):
            for y in xrange(1, n+1):
                v1 = cls.get_sum(BIT, x, y)
                v2 = cls.get_sum(BIT, x-1, y)
                v3 = cls.get_sum(BIT, x, y-1)
                v4 = cls.get_sum(BIT, x-1, y-1)

                cls.updateBIT(BIT, x, y, matrix[x-1][y-1]+v2+v3-v4-v1)

        return BIT

    @classmethod
    def get_sum(cls, BIT, x, y):
        asum = 0

        while x > 0:
            while y > 0:
                asum += BIT[x][y]
                y -= y & (-y)
            x -= x & (-x)

        return asum

    @classmethod
    def updateBIT(cls, BIT, x, y, value):
        while x < len(BIT):
            y1 = y
            while y1 < len(BIT[0]):
                BIT[x][y1] += value
                y1 += y1 & (-y1)
            x += x & (-x)

    @classmethod
    def askQuery(cls, BIT, x1, y1, x2, y2):

        v1 = cls.get_sum(BIT, x2, y2)
        v2 = cls.get_sum(BIT, x2, y1-1)
        v3 = cls.get_sum(BIT, x1-1, y2)
        v4 = cls.get_sum(BIT, x1-1, y1-1)

        return v1-v2-v3+v4


if __name__ == "__main__":
    """
    matrix:              range: (1,2) -> (4,3)
      x                        x
      | 1  2  3  4             | 1  2  3  4
    y --------------->       y ---------------->
    1 | 1  2  3  4           1 | x  2  3  x
    2 | 5  6  7  8           2 | x  6  7  x
    3 | 9  0  1  2           3 | x  0  1  x
    4 | 3  4  5  6           4 | x  4  5  x
      |                        |
      |                        |
    """

    matrix = [[1,2,3,4], \
              [5,6,7,8], \
              [9,0,1,2], \
              [3,4,5,6]]
    BIT = SubMatrixSum.construct_2DBIT(matrix)
    asum = SubMatrixSum.askQuery(BIT, 1, 1, 4, 1)
    print asum

