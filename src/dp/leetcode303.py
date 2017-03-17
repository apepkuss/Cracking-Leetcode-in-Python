

class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.accumulate = [0]
        for i in nums:
            self.accumulate.append(self.accumulate[-1] + i)

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        if i<0 or j>=len(self.accumulate) or i>j:
            return 0
        return self.accumulate[j+1] - self.accumulate[i]
