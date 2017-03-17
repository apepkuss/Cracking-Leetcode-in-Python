import unittest

class Elements(object):
    """
    elements 14.7

    In this problem we consider sets of intervals with integer endpoints; the intervals may be open or closed at
    either end. We want to compute the union of the intervals in such sets. Design an algorithm that takes as input
    a set of intervals, and outputs their union expressed as a set of disjoint intervals.
    """

    @classmethod
    def compute_union(cls, intervals):

        if len(intervals) <= 1:
            return intervals

        intervals.sort(key=lambda interval: interval[0])

        res = []
        start, start_is_closed = intervals[0][0]
        end, end_is_closed = intervals[0][1]
        for i in xrange(1, len(intervals)):
            curr_start, curr_start_is_closed = intervals[i][0]
            curr_end, curr_end_is_closed = intervals[i][1]

            if start <= curr_start <= end:
                if start == curr_start:
                    start_is_closed = start_is_closed or curr_start_is_closed
                    if start == curr_end:
                        start_is_closed = start_is_closed or curr_end_is_closed
                    elif end == curr_end:
                        end_is_closed = end_is_closed or curr_end_is_closed
                    elif end < curr_end:
                        end, end_is_closed = curr_end, curr_end_is_closed

                elif start < curr_start < end:
                    if end == curr_end:
                        end_is_closed = end_is_closed or curr_end_is_closed
                    elif end < curr_end:
                        end, end_is_closed = curr_end, curr_end_is_closed

                elif end == curr_start:
                    if end_is_closed or curr_start_is_closed:
                        end = curr_end
                        end_is_closed = curr_end_is_closed
                    else:
                        res.append(((start, start_is_closed), (end, end_is_closed)))
                        start, start_is_closed = curr_start, curr_start_is_closed
                        end, end_is_closed = curr_end, curr_end_is_closed

            else:
                res.append(((start,start_is_closed), (end,end_is_closed)))
                start, start_is_closed = curr_start, curr_start_is_closed
                end, end_is_closed = curr_end, curr_end_is_closed

            if i == len(intervals) - 1:
                res.append(((start, start_is_closed), (end, end_is_closed)))

        return res


class TestRun(unittest.TestCase):

    def test_case1(self):
        intervals = [((0,False),(3,False)), ((13,False),(15,False)), ((3,True),(4,True)), ((9,False),(11,True)), \
                     ((5,True),(7,False)), ((8,True),(11,False)), ((2,True),(4,True)), ((7,True),(8,False)), \
                     ((12,True),(14,True)), ((12,False),(16,True)), ((1,True),(1,True)), ((16,False),(17,False))]
        res = Elements.compute_union(intervals)
        unittest.TestCase.assertEqual(self, first=[((0,False),(4,True)), ((5,True),(11,True)), ((12,True),(17,False))],\
                                      second=res)


if __name__ == "__main__":
    unittest.main()
