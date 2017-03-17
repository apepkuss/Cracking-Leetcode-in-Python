

class Solution(object):
    """
    @ Google

    Given a sorted integer array where the range of elements are in the inclusive range [lower, upper], return its
    missing ranges.

    For example, given [0, 1, 3, 50, 75], lower = 0 and upper = 99, return ["2", "4->49", "51->74", "76->99"].
    """
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        res = []
        if lower > upper:
            return res
        n = len(nums)
        if n == 0:
            if lower < upper:
                res.append(str(lower)+'->'+str(upper))
            elif lower == upper:
                res.append(str(lower))
            return res
        if lower > nums[n-1]:
            return res
        if upper < nums[0]:
            return res

        for i in range(n):
            if i == 0 and lower < nums[0]:
                d = nums[0] - lower
                if d == 1:
                    res.append(str(lower))
                elif d >= 2:
                    res.append(str(lower)+'->'+str(nums[0]-1))
            if i == n-1 and nums[n-1] < upper:
                d = upper - nums[n-1]
                if d == 1:
                    res.append(str(upper))
                elif d >= 2:
                    res.append(str(nums[n-1]+1)+'->'+str(upper))
            if 0 <= i < n-1:
                d = nums[i+1] - nums[i]
                if d == 2:
                    res.append(str(nums[i]+1))
                elif d > 2:
                    res.append(str(nums[i]+1)+'->'+str(nums[i+1]-1))
        return res