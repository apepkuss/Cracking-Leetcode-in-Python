class Solution(object):
    """
    @ Google

    Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

    If the fractional part is repeating, enclose the repeating part in parentheses.

    For example,

        Given numerator = 1, denominator = 2, return "0.5".
        Given numerator = 2, denominator = 1, return "2".
        Given numerator = 2, denominator = 3, return "0.(6)".

    Hint:

        1. No scary math, just apply elementary math knowledge. Still remember how to perform a long division?
        2. Try a long division on 4/9, the repeating part is obvious. Now try 4/333. Do you see a pattern?
        3. Be wary of edge cases! List out as many test cases as you can think of and test your code thoroughly.
    """
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        # check if both numerator and denominator are positive or negative.
        res = ''
        if (numerator < 0 and denominator > 0) or (numerator > 0 and denominator < 0):
            res = '-'
        num = abs(numerator)
        den = abs(denominator)

        # integral part
        res += str(num / den)
        num %= den
        if num == 0:
            return res

        # fractional part
        res += '.'
        # adict is used to check if current number repeats some number appeared in
        # some previous step.
        # key is the number, value is the position of the number in current string
        adict = {num: len(res)}
        while num != 0:
            num *= 10
            res += str(num / den)
            num %= den
            if num in adict:
                idx = adict[num]
                res = res[:idx] + '(' + res[idx:] + ')'
                break
            adict[num] = len(res)
        return res


if __name__ == "__main__":
    res = Solution().fractionToDecimal(1, 6)
    print res

