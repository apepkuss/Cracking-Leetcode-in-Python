
import unittest

class Solution(object):
    """
    @ Amazon, Microsoft, Bloomberg, Uber

    Implement atoi to convert a string to an integer.

    Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask
    yourself what are the possible input cases.

    Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible
    to gather all the input requirements up front.
    """
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if len(str) == 0:
            return 0

        # remove the leading and tailing whitespace
        s = str.strip()

        # 0: positive, 1: negative
        isNegative = False
        if s[0] == "+" or s[0] == "-":
            if s[0] == "-":
                isNegative = True
            s = s[1:]

        lowerbound, upperbound = 2147483648, 2147483647
        res = 0
        for i in xrange(len(s)):
            if ord(s[i]) < 48 or ord(s[i]) > 57:
                break

            res = res*10 + (ord(s[i])-48)

            # the value exceeds the valid boundaries.
            if isNegative  and res >= lowerbound:
                res = lowerbound
                break
            elif (not isNegative) and res >= upperbound:
                res = upperbound
                break
        return -res if isNegative else res

class TestRun(unittest.TestCase):

    def test_positive(self):
        text = "2147483647"
        actual_result = Solution().myAtoi(text)
        expected_result = 2147483647
        unittest.TestCase.assertEqual(self, first=expected_result, second=actual_result)

    def test_positive_outbound(self):
        text = "2147483648"
        actual_result = Solution().myAtoi(text)
        expected_result = 2147483647
        unittest.TestCase.assertEqual(self, first=expected_result, second=actual_result)

    def test_negative(self):
        text = "-2147483648"
        actual_result = Solution().myAtoi(text)
        expected_result = -2147483648
        unittest.TestCase.assertEqual(self, first=expected_result, second=actual_result)

    def test_negative_outbound(self):
        text = "-2147483649"
        actual_result = Solution().myAtoi(text)
        expected_result = -2147483648
        unittest.TestCase.assertEqual(self, first=expected_result, second=actual_result)

    def test_invalidCharacter(self):
        text = "-21474a83649"
        actual_result = Solution().myAtoi(text)
        expected_result = -21474
        unittest.TestCase.assertEqual(self, first=expected_result, second=actual_result)


if __name__ == "__main__":
    unittest.main()