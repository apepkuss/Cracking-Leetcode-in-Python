

class Vector2D(object):
    """
    @ Google, Airbnb, Twitter, Zenefits

    Implement an iterator to flatten a 2d vector.

    For example,
    Given 2d vector =

    [
      [1,2],
      [3],
      [4,5,6]
    ]
    By calling next repeatedly until hasNext returns false, the order of elements returned by next should be:
    [1,2,3,4,5,6].
    """
    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.arr = []
        self.idx = -2
        if len(vec2d) > 0:
            for i in range(len(vec2d)):
                for j in range(len(vec2d[i])):
                    self.arr.append(vec2d[i][j])
            self.idx = -1

    def next(self):
        """
        :rtype: int
        """
        self.idx += 1
        return self.arr[self.idx]

    def hasNext(self):
        """
        :rtype: bool
        """
        if 0 <= self.idx+1 < len(self.arr):
            return True
        return False