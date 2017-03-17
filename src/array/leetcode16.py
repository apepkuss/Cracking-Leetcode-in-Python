
class Solution(object):
    """
    @ Bloomberg
    """
    def threeSumClosest(self, nums, target): # O(n^2) time
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()     # O(nlog(n))
        import sys
        min_gap = sys.maxint
        res = 0

        for i in range(len(nums)-3+1):  # O(n^2)
            j = i+1
            k = len(nums)-1
            while j < k:
                sum = nums[i]+nums[j]+nums[k]
                gap = abs(target-sum)
                if gap < min_gap:
                    min_gap = gap
                    res = sum
                    if min_gap == 0:
                        return target
                if sum < target: j += 1
                else: k -= 1
        return res
