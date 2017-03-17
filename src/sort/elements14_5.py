import unittest


class Event(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Elements(object):
    """
    elements 14.5:

    Each event is specified as a start time and an end time. Write a program that takes a set of events,
    and determines the maximum number of events that take place concurrently.
    """

    @classmethod
    def compute_max_events(cls, events):  # O(nlogn) time, O(n) space
        if len(events) == 0:
            return 0

        endpoints = []
        for event in events:
            endpoints.append((True, event.start))
            endpoints.append((False, event.end))

        endpoints.sort(key=lambda endpoint: endpoint[1])

        max_concurrent_events = 0
        concurrent_events = 0
        for endpoint in endpoints:
            if endpoint[0]:
                concurrent_events += 1
                max_concurrent_events = max(max_concurrent_events, concurrent_events)
            else:
                concurrent_events -= 1
        return max_concurrent_events


class TestRun(unittest.TestCase):

    def test_case1(self):
        endpoints = [(1,5),(6,10),(11,13),(14,15),(2,7),(8,9),(12,15),(4,5),(9,17)]
        events = []
        for endpoint in endpoints:
            events.append(Event(endpoint[0],endpoint[1]))
        res = Elements.compute_max_events(events)
        unittest.TestCase.assertEqual(self, first=3, second=res)


if __name__ == "__main__":
    unittest.main()

