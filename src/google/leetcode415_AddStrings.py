
class Solution(object):
    """
    @ Google
    Given two non-negative numbers num1 and num2 represented as string, return the sum of num1 and num2.

    Note:

    The length of both num1 and num2 is < 5100.
    Both num1 and num2 contains only digits 0-9.
    Both num1 and num2 does not contain any leading zero.
    You must not use any built-in BigInteger library or convert the inputs to integer directly.
    """
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if len(num1) < len(num2):
            num1, num2 = num2, num1
        res = ''
        carry = 0
        for i in range(-1, -len(num2)-1, -1):
            val1 = ord(num1[i]) - 48
            val2 = ord(num2[i]) - 48
            asum = val1 + val2 + carry
            carry = asum / 10
            val = asum % 10
            res = chr( val +48) + res

        if len(num1) > len(num2):
            i = len(num1) - len(num2) - 1
            while i >= 0 and carry == 1:
                asum = ord(num1[i]) - 48 + carry
                carry = asum / 10
                val = asum % 10
                res = chr( val +48) + res
                i -= 1
            if i >= 0: res = num1[: i +1] + res
        if carry == 1:
            res = '1' + res
        return res


if __name__ == "__main__":
    num1 = "98"
    num2 = "9"
    res = Solution().addStrings(num1, num2)
    print res
