
class Solution(object):
    """
    @ Google

    Given a sorted integer array without duplicates, return the summary of its ranges. For example, given
    [0,1,2,4,5,7], return ["0->2","4->5","7"].
    """
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        res = []
        n = len(nums)
        if n == 0:
            return res
        i = 0
        while i < n:
            if i == n- 1:
                res.append(str(nums[i]))
                break
            r = str(nums[i])
            j = i
            while j + 1 < n and nums[j] + 1 == nums[j + 1]:
                j += 1
            if i != j:
                r += '->' + str(nums[j])
            res.append(r)
            if j == n - 1:
                break
            i = j + 1

        return res

