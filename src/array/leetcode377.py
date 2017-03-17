
class Solution(object):
    """
    @ Google, Snapchat

    Given an integer array with all positive numbers and no duplicates, find the number of possible combinations
    that add up to a positive integer target.

    Follow up:
    What if negative numbers are allowed in the given array?
    Answer: if there was a negative number, then the negative number could generate an infinite number of combinations.
    How does it change the problem?
    What limitation we need to add to the question to allow negative numbers?
    Answer: one way is to limit the number of negative numbers in any possible combinations.
    """

    def combinationSum4_dp(self, nums, target):
        # table[i] indicates the number of the combinations, which sum up to i
        table = [0] * (target + 1)
        table[0] = 1
        for i in xrange(target + 1):
            if table[i] == 0:
                continue
            for j in nums:
                if i + j <= target:
                    table[i + j] += table[i]
        return table[target]

    def combinationSum4_dfs(self, nums, target):  # LTE
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        def dfs(asum):
            if asum > target:
                return
            if asum == target:
                self.res += 1
                return
            for num in nums:
                dfs(asum + num)
            return

        if nums is None or len(nums) == 0:
            return 0
        self.res = 0
        dfs(0)
        return self.res


if __name__ == "__main__":
    nums = [4,2,1]
    target = 32
    res = Solution().combinationSum4_dp(nums, target)
    print res
