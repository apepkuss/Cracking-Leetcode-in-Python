

class Solution(object):
    """
    @ Google

    Given an array of integers where 1 <= a[i] <= n (n = size of array), some elements appear twice and others appear once.

    Find all the elements of [1, n] inclusive that do not appear in this array.

    Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

    Example:

    Input:
    [4,3,2,7,8,2,3,1]

    Output:
    [5,6]
    """

    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        n = len(nums)

        # negate each number in nums
        for i in range(n):
            idx = abs(nums[i])-1
            if nums[idx] > 0:
                nums[idx] = -nums[idx]

        # find out at which index the number is positive, meaning the index
        # was never visited in above for-loop step
        for i in range(n):
            if nums[i] > 0:
                res.append(i+1)

        return res

