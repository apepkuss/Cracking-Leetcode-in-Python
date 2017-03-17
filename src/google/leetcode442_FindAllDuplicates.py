
import collections

class Solution(object):
    """
    @ Pocket Gems

    Given an array of integers, 1 <= a[i] <= n (n = size of array), some elements appear twice and others appear once.

    Find all the elements that appear twice in this array.

    Could you do it without extra space and in O(n) runtime?

    Example:
    Input:
    [4,3,2,7,8,2,3,1]

    Output:
    [2,3]
    """
    def findDuplicates_1(self, nums): # O(n) time, O(n) space
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        htable = collections.defaultdict(int)
        for num in nums:
            htable[num] += 1
        for k, v in htable.items():
            if v > 1:
                res.append(k)
        return res

    def findDuplicates_2(self, nums): # O(n) time, O(1) space
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = []
        for i in range(n):
            idx = abs(nums[i]) - 1
            if nums[idx] > 0:
                nums[idx] = -nums[idx]
            else:
                res.append( idx +1)
        return res