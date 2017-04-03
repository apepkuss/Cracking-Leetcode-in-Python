
class Solution(object):
    """
    @ Linkedin, Microsoft

    Backtracking

    Given a collection of numbers that might contain duplicates, return all possible unique permutations.

    For example,
    [1,1,2] have the following unique permutations:
    [
      [1,1,2],
      [1,2,1],
      [2,1,1]
    ]
    """
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        n = len(nums)
        if n > 0:
            nums.sort()  # to make sure we can skip the same value
            used = [False] * n # to indicate if a value is used or not
            self.backtrack(nums, [], used, res)
        return res

    def backtrack(self, nums, valuelist, used, res):
        if len(valuelist) == len(nums):
            res.append(valuelist)
        else:
            for i in range(len(nums)):
                # if the i-th element has already been used, then go next round
                # if the i-th element is not used, and the i-th and (i-1)-th elements
                # are same, but the (i-1)-th element is also unused, then skip the
                # i-th element
                if used[i] or ( i >0 and nums[ i -1] == nums[i] and used[ i -1] == False):
                    continue

                used[i] = True
                self.backtrack(nums, valuelist + [nums[i]], used, res)
                used[i] = False