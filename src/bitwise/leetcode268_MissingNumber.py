
class Solution(object):
    def missingNumber_bitwise(self, nums):  # RT: O(n)
        """
        :type nums: List[int]
        :rtype: int
        """
        res = len(nums)
        for i in xrange(len(nums)):
            res = res ^ i
            res = res ^ nums[i]
        return res

    def missingNumber_sort(self, nums):  # RT: O(nlogn)
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()  # it's necessary
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) / 2
            if mid != nums[mid]:
                if mid - 1 >= 0 and mid - 1 != nums[mid - 1]:
                    right = mid - 1
                elif mid - 1 == nums[mid - 1]:
                    return mid
                elif mid - 1 < 0:
                    return mid
            else:
                left = mid + 1
                if left == len(nums):
                    return mid + 1
        return -1


if __name__ == "__main__":
    nums = [0,1,2,3,4,6]
    res = Solution().missingNumber_bitwise(nums)
    print res

