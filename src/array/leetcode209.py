
class Solution(object):
    def minSubArrayLen(self, s, nums): # RT: O(n)
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        left, right, sum = 0, 0, 0
        window = size + 1
        while right < size:
            # increase window
            while right < size and sum < s:
                sum += nums[right]
                right += 1
            # decrease window
            while left < right and sum >= s:
                window = min(window, right - left)
                sum -= nums[left]
                left += 1
        return window if window <= size else 0

if __name__ == "__main__":
    mysolution = Solution()
    res = mysolution.minSubArrayLen(7, [8,3,1,2,4,3])
    print res
