
class Solution(object):
    def findMin(self, nums):  # RT: O(logn)
        n = len(nums)
        if nums[0] < nums[-1]:
            return nums[0]
        start, end = 0, n - 1
        while start <= end:
            if start + 1 == end:
                return min(nums[start], nums[end])
            mid = (start + end) / 2
            if nums[mid] < nums[end]:
                end = mid
            elif nums[mid] > nums[end]:
                start = mid
            else:
                return nums[mid]
        return -1
