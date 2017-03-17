
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # the result is a 32-bit integer
        res = 0
        negatives = 0
        for x in xrange(32):
            count = 0
            for i in xrange(len(nums)):
                if nums[i] < 0:
                    nums[i] = ~(nums[i]-1)
                    negatives += 1
                if (nums[i] >> x) & 1 == 1:
                    count += 1
            bit = count % 3
            if bit == 1:
                res |= bit << x
        return res if negatives % 3 == 0 else -res
