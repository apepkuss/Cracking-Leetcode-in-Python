
class Solution(object):
    """
    @ Google

    Write a program to find the nth super ugly number. Super ugly numbers are positive numbers whose all prime
    factors are in the given prime list primes of size k. For example, [1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28, 32]
    is the sequence of the first 12 super ugly numbers given primes = [2, 7, 13, 19] of size 4.

    Note:
    (1) 1 is a super ugly number for any given primes.
    (2) The given numbers in primes are in ascending order.
    (3) 0 < k <= 100, 0 < n <= 106, 0 < primes[i] < 1000.
    """
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        res = [1]
        if n == 1: return res[-1]
        nums = [1] * len(primes)
        idx = [0] * len(primes)
        curr = 1
        for i in range( n -1):
            for j in range(len(primes)):
                if nums[j] == curr:
                    nums[j] = res[idx[j]] * primes[j]
                    idx[j] += 1
            curr = min(nums)
            res.append(curr)
        return res[-1]
