

class Solution(object):
    """
    @ Google
    
    Given an array of n integers nums and a target, find the number of index triplets i, j, k with 0 <= i < j < k < n
    that satisfy the condition nums[i] + nums[j] + nums[k] < target.

    For example, given nums = [-2, 0, 1, 3], and target = 2.

    Return 2. Because there are two triplets which sums are less than 2:

    [-2, 0, 1]
    [-2, 0, 3]
    Follow up:
    Could you solve it in O(n2) runtime?
    """
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        nums.sort()
        count = 0
        for i in range(n-2):
            l, r = i+1, n-1
            while l < r:
                if nums[i] + nums[l] + nums[r] < target:
                    count += r - l
                    l += 1
                else:
                    r -= 1
        return count