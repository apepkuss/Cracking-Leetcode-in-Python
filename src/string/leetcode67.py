import unittest


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if len(a) == 0:
            return b
        elif len(b) == 0:
            return a

        # a is longer than b
        if len(a) < len(b):
            a, b = b, a

        # convert string into list for manipulating character
        alist = list(a)
        blist = list(b)

        carry = 0
        for i in xrange(-1, -len(blist)-1, -1):
            if alist[i] == '1' and blist[i] == '1':
                alist[i] = str(carry)
                carry = 1
            elif alist[i] == '0' and blist[i] == '0':
                alist[i] = str(carry)
                carry = 0
            else: # (a[i]=='1' and b[i]=='0') or (a[i]=='0' and b[i]=='1')
                alist[i] = str((1+carry)%2)
                carry = (1+carry)/2  # Bug: carry=0

        j = -len(blist)-1
        while carry == 1 and j >= -len(alist):
            if alist[j] == '1':
                alist[j] = str(0)
                carry = 1
                j -= 1
            else:
                alist[j] = str(1)
                carry = 0
                break

        if carry == 1 and j < -len(alist):
            return "".join(["1"] + alist)
        else:
            return "".join(alist)


class TestRun(unittest.TestCase):

    def test_case1(self):
        a = "101111"
        b = "111"
        actual_result = Solution().addBinary(a, b)
        expected_result = "110110"
        unittest.TestCase.assertEqual(self, first=expected_result, second=actual_result)


if __name__ == "__main__":
    unittest.main()

