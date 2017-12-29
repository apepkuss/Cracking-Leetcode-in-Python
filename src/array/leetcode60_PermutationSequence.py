
class Solution(object):
    def getPermutation(self, n, k): # O(n)
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        assert n > 0
        nums = [str(x + 1) for x in range(n)]

        # compute the factorial of (n-1)
        fact = 1
        for i in range(1, n):
            fact *= i

        res = ''
        x = n-1
        while x > 0 and nums:
            i = k / fact
            k = k % fact
            print('k: %d, fact: %d, i: %d' % (k, fact, i))

            print('Before updating nums: {0}'.format(nums))
            if k == 0:
                if i == 0:
                    res += ''.join(nums)
                else:
                    res += str(nums[i-1])
                    nums.remove(nums[i-1])
                    res += ''.join(nums[::-1])
                nums = []
            else:
                res += str(nums[i])
                nums.remove(nums[i])
            print('After update, nums: {0}, res: {1}'.format(nums, res))

            # update fact
            fact = fact / x
            x -= 1

        return res


if __name__ == "__main__":
    mysolution = Solution()
    res = mysolution.getPermutation(n=6, k=400)
    print res
