import unittest


class Elements(object):
    """
    elements 14.14 Compute a salary threshold

    ABC corporation needs to cut payroll expenses to a specified target. The chief executive officer wants to do
    this by putting a cap on last year's salaries. Every employee who earned more than the cap last year will be
    paid the cap this year; employees who earned no more than the cap will see no change in their salary.

    Design an algorithm for computing the salary cap, given existing salaries and the target payroll.
    """

    @classmethod
    def compute_cap(cls, salaries, target_payroll):   # O(nlogn) time

        # sort salaries in increasing order
        salaries.sort()

        asum = 0
        n = len(salaries)
        for i in xrange(n):
            payroll = salaries[i] * (n-i) + asum
            if payroll == target_payroll:
                return salaries[i]
            elif payroll > target_payroll:
                return (target_payroll - asum) / 2
            else:
                asum += salaries[i]
        return -1


class TestRun(unittest.TestCase):

    def test_case1(self):
        salaries = [90, 30, 100, 40, 20]
        target_payroll = 210
        res = Elements.compute_cap(salaries, target_payroll)
        unittest.TestCase.assertEqual(self, first=60, second=res)


if __name__ == "__main__":
    unittest.main()
