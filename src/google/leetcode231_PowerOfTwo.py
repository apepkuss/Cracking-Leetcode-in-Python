

class Solution(object):
    """
    @ Google
    Given an integer, write a function to determine if it is a power of two.
    """
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while (n&1)==0 and n>0:
            n>>=1
        return n==1