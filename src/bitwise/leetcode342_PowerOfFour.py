
import math
class Solution(object):
    """
    @ Two Sigma
    
    Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

    Example:
    Given num = 16, return true. Given num = 5, return false.

    Follow up: Could you solve it without loops/recursion?
    """

    def isPowerOfFour_NoLoop(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return False if num <= 0 else num == round(4**round(math.log(num, 4)))
    
    def isPowerOfFour_recursive(self, num):
        if num <= 0: return False
        if num == 1: return True
        return num % 4 == 0 and self.isPowerOfFour(num / 4)
    
    def isPowerOfFour_Loop(self, num):
        if num <= 0: return False
        if num == 1: return True
        while num != 1:
            if num % 4 == 0:
                num /= 4
            else: return False
        return True
    
    def isPowerOfFour_bitwise(self, num):
        if num == 0:
            return False
        if num == 1: 
            return True
        val = num & 0x55555554
        if val == 0:
            return False
        while val & 1 == 0:
            val = val >> 1
        val = val >> 1
        if val == 0:
            return num & 0xAAAAAAAB == 0
        else:
            return False