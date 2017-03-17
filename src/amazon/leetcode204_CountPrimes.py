
class Solution(object): # IMPORTANT PROBLEM
    """
    @ Amazon, Microsoft

    Hash Table, Math

    Description: Count the number of prime numbers less than a non-negative number, n.
    """

    # The following algorithm is Simple Sieve, in which n is smaller than 10 million.
    # Therefore, the issues in Simple Sieve:
    #   1. the size of list may not fit it memory
    #   2. not cache friendly even for slightly bigger n. The algorithm traverses the list
    #      without locality of reference.
    def countPrimes_simpleSieve(self, n): # algorithm of sieve of Eratosthenes
        """
        :type n: int
        :rtype: int
        """
        if n<= 2:
            return 0

        primes = [1 for x in range(n)]  # This step is critical. You cannot use the way of removing a non-prime number
        # from a list, then computing the length the list to get the result, as it causes
        # "time limit exceeded" error.
        p = 2
        while p * p < n:
            if primes[p] == 1:
                for i in range(p * 2, n, p):
                    primes[i] = 0
            p += 1

        return sum(primes[2::])


    # Segmented Sieve improves Simple Sieve.
    # The idea of segmented sieve is to divide the range [0...n-1] into several different segments and
    # compute primes in all segments one by one. This algorithm first uses Simple Sieve to find all primes
    # smaller than or equal to the square root of n.

    def countPrimes_segmentedSieve(self, n):

        def simpleSieve(limit):
            mark = [True] * limit

            p = 2
            while p*p < limit:
                if mark[p]:
                    for i in range(p*2, limit, p):
                        mark[i] = False
                p += 1

            mark = [value for value in mark if value]
            return mark

        import math

        limit = math.floor(math.sqrt(n))
        primes = simpleSieve(limit)

        res = len(primes)

        # divide the range [0...n-1] into different segements, and
        # the size of each segment is limit
        low = limit
        high = limit * 2

        while (low < n):

            # to mark primes in current section
            # A value in mark[i] will be False if the number of (i-low) is not a prime; otherwise, True.
            mark = [True] * (limit)

            # use the primes returned from Simple Sieve to compute the primes in current section
            for i in range(len(primes)):
                # find the minimum number in [low...high], which is a multiple of primes[i]
                multiple = math.floor(low / primes[i]) * primes[i]
                if multiple < low:
                    multiple += primes[i]

                # mark multiples of primes[i] in [low...high]
                for j in range(multiple, high, primes[i]):
                    mark[j] = False

            # count the number of primes in current section
            res += mark.count(True)

            # increase low and high by one limit
            low += limit
            high += limit
            if high >= n: high = n

        return res







