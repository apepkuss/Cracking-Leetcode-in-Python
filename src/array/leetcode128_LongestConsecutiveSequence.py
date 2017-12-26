
class Solution(object):
    """
    Given an unsorted array of integers, find the length of the longest consecutive
    elements sequence. For example, Given [100, 4, 200, 1, 3, 2], The longest consecutive
    elements sequence is [1, 2, 3, 4]. Return its length: 4. Your algorithm
    should run in O(n) complexity.
    """
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        assert nums is not None

        if len(nums) <= 1:
            return len(nums)

        adict = {}
        for i in nums:
            adict[i] = False

        maxlen = 0
        for i in nums:
            if adict[i]:
                continue
            adict[i] = True
            cur_lcs = 1

            # check the consecutivity of the right
            # side of the current key
            j = i+1
            while j in adict:
                adict[j] = True
                j += 1
                cur_lcs += 1

            # check the consecutivity of the left
            # side of the current key
            j = i-1
            while j in adict:
                adict[j] = True
                j -= 1
                cur_lcs += 1

            # update the length of LCS
            maxlen = max(maxlen, cur_lcs)
            if maxlen == len(nums):
                break

        return maxlen
