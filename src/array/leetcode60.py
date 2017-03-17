
class Solution(object):
    def getPermutation(self, n, k): # O(n)
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        res = ''
        # compute the factorial of (n-1)
        factorial = 1
        for i in xrange(1,n):
            factorial *= i
        nums = [x+1 for x in xrange(n)]
        for x in xrange(n-1, 0, -1):
            i = k/factorial
            k = k%factorial
            if k > 0:
                res += str(nums[i])
                nums.remove(nums[i])
            else:
                res += str(nums[i-1])
                nums.remove(nums[i-1])
            factorial = factorial / x
        res += str(nums[0])
        return res

if __name__ == "__main__":
    mysolution = Solution()
    res = mysolution.getPermutation(n=6, k=400)
    print res
