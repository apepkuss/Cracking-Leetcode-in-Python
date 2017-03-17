
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):  # RT: O(n)
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        res = []
        n = len(intervals)
        if n == 0:
            res.append(newInterval)
            return res
        i = 0
        while i < n:
            if intervals[i].end < newInterval.start:
                res.append(intervals[i])
                i += 1
            else:
                break

        if i == n:
            res.append(newInterval)

        while i < n:
            if newInterval.end < intervals[i].start:
                res.append(newInterval)
                break
            if intervals[i].start <= newInterval.end <= intervals[i].end:
                newInterval.start = min(newInterval.start, intervals[i].start)
                newInterval.end = intervals[i].end
                res.append(newInterval)
                i += 1
                break
            else:
                newInterval.start = min(newInterval.start, intervals[i].start)
                i += 1
                if i == n:
                    res.append(newInterval)
                    break

        while i < n:
            res.append(intervals[i])
            i += 1

        return res