

class Solution(object):
    def firstMissingPositive_1(self, nums): # O(n) time, O(n) space
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 1
        n = len(nums)
        table = [False for _ in xrange(n+1)]
        for i in xrange(n):
            if 1<=nums[i]<=n:
                table[nums[i]] = True
        for i in xrange(1, n+1):
            if table[i] is False:
                return i
        return len(table)

    def firstMissingPositive_2(self, nums):  # O(n) time, O(1) space
        """
        :type nums: List[int]
        :rtype: int
         Basic idea:
        1. for any array whose length is l, the first missing positive must be in range [1,...,l+1],
            so we only have to care about those elements in this range and remove the rest.
        2. we can use the array index as the hash to restore the frequency of each number within
             the range [1,...,l+1]
        """
        nums.append(0)
        n = len(nums)
        for i in xrange(len(nums)):  # delete those useless elements
            if nums[i] < 0 or nums[i] >= n:
                nums[i] = 0
        for i in xrange(len(nums)):  # use the index as the hash to record the frequency of each number
            nums[nums[i] % n] += n
        for i in xrange(1, len(nums)):
            if nums[i] / n == 0:
                return i
        return n

if __name__ == "__main__":
    mysolution = Solution()
    res = mysolution.firstMissingPositive_2([1,2,0])
    print res
