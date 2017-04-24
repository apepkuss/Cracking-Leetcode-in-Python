

class Solution(object):
    """
    @ Microsoft, Apple
    
    Bit Manipulation
    
    Write a function that takes an unsigned integer and returns the number of '1' bits it has 
    (also known as the Hamming weight).

    For example, the 32-bit integer '11' has binary representation 00000000000000000000000000001011, 
    so the function should return 3.
    """

    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        while n:
            if n & 1:
                res += 1
            n >>= 1
        return res
