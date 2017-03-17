
class Solution(object):
    def spiralOrder(self, matrix):
        res = []
        if matrix==[]: return res
        m, n = len(matrix), len(matrix[0])
        top, bottom = 0, m-1
        left, right = 0, n-1
        # direct indicates the direction of current move
        # 0:to right, 1:downwards, 2:to left, 3:upwards
        direct = 0
        while True:
            if direct==0:
                for y in xrange(left, right+1):
                    res.append(matrix[top][y])
                top += 1
            if direct==1:
                for x in xrange(top, bottom+1):
                    res.append(matrix[x][right])
                right -= 1
            if direct==2:
                for y in xrange(right, left-1, -1):
                    res.append(matrix[bottom][y])
                bottom -= 1
            if direct==3:
                for x in xrange(bottom, top-1, -1):
                    res.append(matrix[x][left])
                left += 1
            if top>bottom or left>right: return res
            direct = (direct+1) % 4
