
import math

class Solution(object):
    """
    @ Google

    Given an integer, write a function to determine if it is a power of three.

    Follow up:
    Could you do it without using any loop / recursion?
    """
    def isPowerOfThree_NoLoop(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return False if n <= 0 else n == round(3**round(math.log(n, 3)))

    def isPowerOfThree_Loop(self, n):
        if n <= 0: return False
        if n == 1: return True
        while n != 1:
            if n % 3 == 0:
                n /= 3
            else: return False
        return True
        
    def isPowerOfThree_recursive(self, n):
        if n <= 0: return False
        if n == 1: return True
        return n % 3 == 0 and self.isPowerOfThree(n/3)