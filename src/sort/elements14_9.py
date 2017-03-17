import unittest


class Elements(object):
    """
    elements 14.9: compute an optimum assignment of tasks

    Consider the problem of scheduling tasks to be performed by workers. Each worker must be assigned exactly two
    tasks. Each task has a duration. Tasks are independent, i.e., there are no constraints fo the form "Task 4 cannot
    start before Task 3 is completed."

    Design an algorithm that takes as input an array of numbers, which are the durations of the tasks, and computes a
    set of pairs of tasks such that the maximum pair sum is minimum. Each task must be in exactly one pair.
    """

    @classmethod
    def task_assignment(cls, durations):  # O(nlogn) time
        res = []
        if durations is None:
            return res

        # sort the durations
        durations.sort()

        i, j = 0, len(durations)-1
        while i <= j:
            res.append((durations[i], durations[j]))
            i += 1
            j -= 1

        return res


class TestRun(unittest.TestCase):

    def test_case1(self):
        durations = [5,2,1,6,4,4]
        res = Elements.task_assignment(durations)
        unittest.TestCase.assertEqual(self, first=[(1,6), (2,5), (4,4)], second=res)


if __name__ == "__main__":
    unittest.main()