import unittest


class Elements(object):
    """
    elements 14.13 Compute the smallest nonconstructible change

    Suppose you have some coins. There are some amounts of change that you may not be able to make with
    these coins, e.g., you cannot create a change amount greater than the sum of the coin's denominations.
    For example, if your coins have denomination 1, 1, 1, 1, 5, 10, 25, then the smallest value of change
    which cannot be made is 20.

    Write a function which takes an array of positive integers and returns the smallest number which is not
    to the sum of a subset of elements of the array.
    """

    @classmethod
    def compute_smallest_nonconstructible(cls, denominations):

        if denominations is None or len(denominations)==0:
            return 0

        # sort denominations
        denominations.sort()

        sum_up = denominations[0]
        for i in xrange(1, len(denominations)):
            if denominations[i] <= sum_up+1:
                sum_up += denominations[i]
            else:
                return sum_up + 1
        return sum_up + 1


class TestRun(unittest.TestCase):

    def test_case1(self):
        denominations = [12,2,1,15,2,4]
        res = Elements.compute_smallest_nonconstructible(denominations)
        unittest.TestCase.assertEqual(self, first=10, second=res)


if __name__ == "__main__":
    unittest.main()
