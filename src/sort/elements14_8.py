import unittest


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Elements(object):
    """
    elements 14.8: the interval covering problem

    Consider an engineer responsible for a number of tasks on the factory floor. Each task starts at a fixed time and
    ends at a fixed time. The engineer wants to visit the floor to check on the tasks. Your job is to help him minimize
    the number of visits he makes. In each visit, he can check on all the tasks taking place at the time of the visit.
    A visit takes place at a fixed time, and he can only check on tasks taking place at exactly that time. For example,
    if there are tasks at times [0,3], [2,6], [3,4], [6,9], then visit times 0, 2, 3, 6 cover all tasks. A smaller set
    of visit times that also cover all tasks is 3, 6. In the abstract, you are to solve the following problem.

    You are given a set of closed intervals. Design an efficient algorithm for finding a minimum number of numbers that
    cover all the intervals.
    """

    @classmethod
    def compute_minimal_times(cls, intervals):
        res = []
        visit_times = 0
        if intervals is None or len(intervals)==0:
            return res

        # first, sort intervals by their end's values
        intervals.sort(key=lambda x: x.end)

        # second, pop out the leftmost interval from sorted intervals, whose end is smallest; then,
        # iterate the remaining intervals: if anyone is covered by the interval's end value, then add it to the
        # covered_intervals dictionary. Repeat the procedure until intervals is empty.
        covered_intervals = {}
        while len(intervals) > 0:
            leftmost_interval = intervals.pop(0)
            if covered_intervals.has_key(leftmost_interval):
               continue

            while len(intervals) > 0:
                curr_interval = intervals[0]
                if curr_interval.start <= leftmost_interval.end <= curr_interval.end:
                    if not covered_intervals.has_key(curr_interval):
                        covered_intervals[curr_interval] = True
                    intervals.pop(0)
                else:
                    break
            res.append(leftmost_interval.end)
            visit_times += 1

        return res


class TestRun(unittest.TestCase):

    def test_case1(self):
        tasks = [(1,2),(2,3),(3,4),(2,3),(3,4),(4,5)]
        intervals = []
        for task in tasks:
            intervals.append(Interval(task[0], task[1]))
        res = Elements.compute_minimal_times(intervals)
        # unittest.TestCase.assertEqual(self, first=2, second=res)
        unittest.TestCase.assertEqual(self, first=[2,4], second=res)


if __name__ == "__main__":
    unittest.main()
