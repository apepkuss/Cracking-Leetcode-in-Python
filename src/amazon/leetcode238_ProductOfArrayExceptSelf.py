
class Solution(object):
    """
    @ Amazon, Linkedin, Apple, Facebook, Microsoft
    
    Array

    Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to
    the product of all the elements of nums except nums[i].

    Solve it without division and in O(n).

    For example, given [1,2,3,4], return [24,12,8,6].

    Follow up:
    Could you solve it with constant space complexity? (Note: The output array does not count as extra space
    for the purpose of space complexity analysis.)
    """

    # Use two round iterations:
    # 1. the first iteration is from left to right, res[i] denotes the product of the first i elements
    # 2. the second iteration is from right to left, res[i] denotes the product of both the first i elements
    #    and the remaining elements from i+1 to the end.
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = [1] * n

        product = 1
        # first iteration to get the product of first i elements
        # res[i] denotes the product of first i elements except the element at index of i
        for x in xrange(n-1):
            product *= nums[x]
            res[x+1] *= product

        product = 1
        # second iteration to get the product of both first i elements and the elements from i+1 to the end.
        # res[i] denotes the product of all elements except the element at index of i
        for x in xrange(n-1, 0, -1):
            product *= nums[x]
            res[x-1] *= product
        return res
