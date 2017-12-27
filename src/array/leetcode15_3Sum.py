class Solution(object):
    """
    @ Amazon, Microsoft, Bloomberg, Facebook, Adobe

    Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets
    in the array which gives the sum of zero.

    Note: The solution set must not contain duplicate triplets.

    For example, given array S = [-1, 0, 1, 2, -1, -4],
    A solution set is:
    [
      [-1, 0, 1],
      [-1, -1, 2]
    ]
    """

    def threeSum_dfs(self, nums, target):
        assert nums is not None
        if len(nums) < 3:
            return []

        res = set()
        self.dfs(nums, target, [], res)
        return [list(elem) for elem in res]

    def dfs(self, nums, target, valuelist, res):
        if target == 0 and len(valuelist) == 3:
            res.add(tuple(valuelist))
        elif len(valuelist) < 3:
            for i in range(len(nums) + len(valuelist) - 2):
                val = nums[i]
                self.dfs(nums[i + 1:], target - val, valuelist + [val], res)

    def threeSum_Generic(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def ksum(nums, k, target):
            # This is a generic k-sum algorithm
            res = set()  # avoid duplicates
            i = 0
            if k == 2:
                j = len(nums) - 1
                # the code in while-loop below can work because nums is sorted
                while i < j:
                    if nums[i] + nums[j] == target:
                        res.add((nums[i], nums[j]))
                        i += 1
                    elif nums[i] + nums[j] > target:
                        j -= 1
                    else:
                        i += 1

            # case: k>2
            else:
                for i in xrange(len(nums) - k + 1):
                    subresult = ksum(nums[i + 1:], k - 1, target - nums[i])
                    if subresult:
                        res = res | set((nums[i],) + nr for nr in subresult)
            return res

        nums.sort()  # O(nlog(n))
        return [list(t) for t in ksum(nums, 3, 0)]
