
class Solution(object):
    """
    @ Google

    Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...

    Note:
    n is positive and will fit within the range of a 32-bit signed integer (n < 231).

    Example 1:

    Input:
    3

    Output:
    3
    Example 2:

    Input:
    11

    Output:
    0

    Explanation:
    The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.

    """
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        digit, base = 1, 9
        while True:
            digits = base * (10**(digit-1)) * digit
            if n > digits:
                n -= digits
                digit += 1
            else:
                break
        val = 10**(digit-1) + n/digit - 1
        rem = n % digit
        if rem == 0:
            return val % 10
        elif rem == 1:
            return (val+1) / (10**(digit-1))
        else:
            return (val+1) / (10**(digit-rem)) % 10