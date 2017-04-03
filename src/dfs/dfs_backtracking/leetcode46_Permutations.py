
class Solution(object):
    """
    @ Linkedin, Microsoft

    Backtracking

    Given a collection of distinct numbers, return all possible permutations.

    For example,
    [1,2,3] have the following permutations:
    [
      [1,2,3],
      [1,3,2],
      [2,1,3],
      [2,3,1],
      [3,1,2],
      [3,2,1]
    ]
    """

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        n = len(nums)

        if n > 0:
            self.backtrack(nums, [], res)

        return res

    def backtrack(self, nums, valuelist, res):
        if len(valuelist) == len(nums):
            res.append(valuelist)
        else:
            for i in range(len(nums)):
                if nums[i] not in valuelist:
                    self.backtrack(nums, valuelist + [nums[i]], res)

if __name__ == "__main__":
    nums = [1, 2, 3]
    res = Solution().permute(nums)
    print res
