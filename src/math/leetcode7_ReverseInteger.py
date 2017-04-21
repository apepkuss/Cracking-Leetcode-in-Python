

class Solution(object):
    """
    @ Bloomberg, Apple
    
    Math
    
    Reverse digits of an integer.

    Example1: x = 123, return 321
    Example2: x = -123, return -321
    
    click to show spoilers.
    
    Note:
    The input is assumed to be a 32-bit signed integer. Your function 
    should return 0 when the reversed integer overflows.
    """

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = 0
        lower, upper = - 2 **31, 2** 31 - 1

        negative = False
        if x < 0:
            negative = True
            x = -x

        while x > 0:
            i = x % 10
            res = res * 10 + i
            # check overflow
            if res < lower or res > upper:
                return 0
            x = x / 10

        return -res if negative else res


if __name__ == "__main__":
    res = Solution().reverse(1534236469)
    print res
