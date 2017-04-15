

class Solution(object):
    """
    @ Bloomberg, Apple, Facebook
    
    Binary Search, Math
    
    Implement int sqrt(int x).

    Compute and return the square root of x.
    """
    def mySqrt(self, x):  # O(logn) time
        """
        :type x: int
        :rtype: int
        """
        if x == 0: return 0
        left, right = 1, 2**32-1
        while True:
            mid = left + (right - left) / 2
            if mid > x / mid:
                right = mid - 1
            else:
                if mid+1 > x / (mid+1):
                    return mid
                left = mid + 1