

# Definition for a point.
class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


class Solution(object):
    """
    @ Linkedin, Apple, Twitter
    
    Hashtable, Math
    
    Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.
    """
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        res = 0
        if not points: return res

        adict = {}
        n = len(points)
        for i in range(n):
            count = 0  # the maximum number of points lying on the line from points[i]
            overlap = 0  # the number of points overlapping with points[j]
            for j in range(i + 1, n):
                x = points[i].x - points[j].x
                y = points[i].y - points[j].y

                # points[i] overlaps with point[j]
                if x == 0 and y == 0:
                    overlap += 1
                    continue

                # compute GCD
                gcd = self.get_gcd(x, y)
                if gcd != 0 and gcd != 1:
                    x /= gcd
                    y /= gcd

                key = (points[i], x, y)
                if key in adict:
                    adict[key] += 1
                else:
                    adict[key] = 1

                count = max(count, adict[key])

            res = max(res, count + overlap + 1)
        return res

    def get_gcd(self, x, y):
        """Get greatest common divisor of x and y"""
        if y == 0:
            return x
        return self.get_gcd(y, x % y)


if __name__ == "__main__":
    points = [Point(0,0), Point(-1,-1), Point(2,2)]
    res = Solution().maxPoints(points)
    print res


