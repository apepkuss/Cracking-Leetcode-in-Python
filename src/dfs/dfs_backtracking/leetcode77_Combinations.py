
class Solution(object):
    """
    Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

    For example,
    If n = 4 and k = 2, a solution is:

    [
      [2,4],
      [3,4],
      [2,3],
      [1,2],
      [1,3],
      [1,4],
    ]
    """
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        nums = [i for i in range(1, n+1)]
        self.backtrack(nums, k, [], res)
        return res

    def backtrack(self, nums, k, valuelist, res):
        if k == 0:
            res.append(valuelist)
        elif len(nums) >= k:
            for i in range(len(nums)):
                # the first argument is nums[i+1:] because next number must
                # be greater than all previous numbers in valuelist
                self.backtrack(nums[i+1:], k - 1, valuelist + [nums[i]], res)
