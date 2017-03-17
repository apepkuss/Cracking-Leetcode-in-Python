
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # basic XOR operations: x^x=0, x^0=x
        # Suppose nums=[2,2,3,4,4], 2^2^3^4^4=(2^2)^3^(4^4)=3
        # Suppose nums=[2,1,3,2,3], 2^1^3^2^3=3^2^3=1^3=1
        sn = nums[0]
        for i in range(1, len(nums)):
            sn = sn ^ nums[i]

        return sn