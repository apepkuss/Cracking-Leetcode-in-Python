
class Solution(object):

    # Method 1
    def lengthOfLIS_dp1(self, nums):  # O(n^2) time, O(n^2) space
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n== 0: return n

        # dp[i] denotes the length of LIS of nums[0..i]
        dp = [1 for _ in xrange(n)]

        for i in xrange(n):
            for j in xrange(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

    # Method 2
    # The analysis can be referenced in
    # http://www.geeksforgeeks.org/longest-monotonically-increasing-subsequence-size-n-log-n/
    def lengthOfLIS_dp2(self, nums): # O(nlogn) time, O(n) space
        n = len(nums)
        if n == 0: return n
        # dp[i] indicates the value of end element in the sequence of length i.
        dp = [nums[0]]
        lengthOfLSI = 1
        for i in range(1, n):
            if nums[i] < dp[0]:
                dp[0] = nums[i]
            elif nums[i] > dp[-1]:
                dp.append(nums[i])
                lengthOfLSI += 1
            else:
                # The parameter 'left' in getCeilIndex function MUST be -1,
                # because have to consider the case in which there are just
                # two elements.
                ceilIndex = self.getCeilIndex(dp, -1, len(dp) - 1, nums[i])
                dp[ceilIndex] = nums[i]
        return lengthOfLSI

    def getCeilIndex(self, dp, left, right, key):
        while right - left > 1:
            mid = left + (right - left) / 2
            if dp[mid] >= key:
                right = mid
            else:
                left = mid
        return right

if __name__ == "__main__":
    mysolution = Solution()
    res = mysolution.lengthOfLIS_dp2([4,10,4,3,8,9])
    print res

