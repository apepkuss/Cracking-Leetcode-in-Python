
import collections

class Solution(object):
    """
    @ Google

    Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k) such that
    the distance between i and j equals the distance between i and k (the order of the tuple matters).

    Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of points are all in the
    range [-10000, 10000] (inclusive).

    Example:
    Input:
    [[0,0],[1,0],[2,0]]

    Output:
    2

    Explanation:
    The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]
    """
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res = 0
        for x1, y1 in points:
            htable = collections.defaultdict(int)
            for x2, y2 in points:
                htable[(x2 - x1) ** 2 + (y2 - y1) ** 2] += 1
            for v in htable.values():
                res += v * (v - 1)

        return res


if __name__ == "__main__":
    points = [[0,0],[1,0],[-1,0],[0,1],[0,-1]]
    res = Solution().numberOfBoomerangs(points)
    print res

