
class Solution(object):
    """
    @ Amazon, Uber, Facebook

    Given a set of distinct integers, nums, return all possible subsets.

    Note: The solution set must not contain duplicate subsets.

    For example,
    If nums = [1,2,3], a solution is:

    [
      [3],
      [1],
      [2],
      [1,2,3],
      [1,3],
      [2,3],
      [1,2],
      []
    ]
    """
    def subsets_dfs(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(start, valuelist):
            # No necessary to judge if valuelist is in res
            # because all integers are distinct.
            res.append(valuelist)

            for i in range(start, len(nums)):
                dfs(i+1, valuelist+[nums[i]])

        # not necessary to sort the array first, because all integers are distinct.
        # nums.sort()
        res = []
        dfs(0, [])
        return res

    def subsets_iterative(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for num in nums:
            res += [item + [num] for item in res]
        return res

    # The idea is that to give all the possible subsets, we just need to exhaust all the possible combinations
    # of the numbers. And each number has only two possibilities: either in or not in a subset. And this can be
    # represented using a bit.
    def subsets_BitManipulation(self, nums):
        n = len(nums)
        num_subset = pow(2, n)
        res = [[] for _ in range(num_subset)]
        for i in range(n):
            for j in range(num_subset):
                flag = (j >> i) & 1
                if (j >> i) & 1:
                    res[j].append(nums[i])
        return res


if __name__ == "__main__":
    nums = [3,7,11]
    res = Solution().subsets_dfs(nums)
    print res
