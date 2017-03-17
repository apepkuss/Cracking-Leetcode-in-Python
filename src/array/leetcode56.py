
class Solution(object):
    def merge(self, intervals):  # O(n) time
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals.sort(key=lambda x:x.start)

        m = len(intervals)
        res = []
        if m==0: return res

        curr = intervals[0]
        for x in range(1, m):
            if intervals[x].start <= curr.end:
                curr.end = max(curr.end, intervals[x].end)
            else:
                res.append(curr)
                curr = intervals[x]
        res.append(curr)
        return res
