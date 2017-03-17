


class Solution(object):
    """
    @ Google

    Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies: Si % Sj = 0 or Sj % Si = 0.

    If there are multiple solutions, return any subset is fine.

    Example 1:

        nums: [1,2,3]
        Result: [1,2] (of course, [1,3] will also be ok)

    Example 2:
        nums: [1,2,4,8]

        Result: [1,2,4,8]
    """
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        if n == 0:
            return []
        nums.sort()
        table = [[]] * n
        table[0] = [nums[0]]
        maxidx = 0
        for i in range(1, n):
            table[i] = [nums[i]]
            for j in range(i-1, -1, -1):
                if nums[i] % nums[j] == 0 or nums[j] % nums[i] == 0:
                    if len(table[i]) <= len(table[j]):
                        table[i] = table[j] + [nums[i]]
            if len(table[maxidx]) < len(table[i]):
                maxidx = i
        return table[maxidx]


if __name__ == "__main__":
    nums = [3,4,16,8]
    res = Solution().largestDivisibleSubset(nums)
    print res

