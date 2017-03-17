
class MovingAverage(object):
    """
    @ Google

    Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

    For example,
    MovingAverage m = new MovingAverage(3);
    m.next(1) = 1
    m.next(10) = (1 + 10) / 2
    m.next(3) = (1 + 10 + 3) / 3
    m.next(5) = (10 + 3 + 5) / 3
    """
    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.size = size
        self.queue = []
        self.asum = 0.0


    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.queue.append(val)
        self.asum += val
        if self.size >= len(self.queue):
            return self.asum / len(self.queue)
        else:
            self.asum -= self.queue.pop(0)
            return self.asum / self.size