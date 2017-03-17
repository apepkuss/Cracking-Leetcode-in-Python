
import unittest


class Elements(object):
    """
    elements55: write a function that multiplies two non-negative integers. The only
    operators you are allowed to use are assignment and the bitwise operators, i.e.,
    >>, <<, &, |, ~, ^. You cannot use increment and decrement. You may use loops,
    conditionals and functions that you write yourself.
    """
    @classmethod
    def multiply_bitwise(cls, x, y):
        sum = 0
        while x:
            if x & 1:
                sum = cls.add_bitwise(sum, y)
            x >>= 1
            y <<= 1
        return sum

    @classmethod
    def add_bitwise(cls, a, b):
        sum = 0
        tmp_a = a
        tmp_b = b
        carryin = 0
        k = 1
        while tmp_a or tmp_b:
            ak = a & k
            bk = b & k
            carryout = (ak & bk) | (ak & carryin) | (bk & carryin)
            sum |= ak ^ bk ^ carryin
            carryin = carryout << 1
            tmp_a >>= 1
            tmp_b >>= 1
            k <<= 1
        return sum | carryin


class RunTest(unittest.TestCase):

    def test_case1(self):
        res = Elements.multiply_bitwise(3, 5)
        unittest.TestCase.assertEqual(self, first=15, second=res)


if __name__ == "__main__":
    unittest.main()
