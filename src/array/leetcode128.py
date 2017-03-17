
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)

        # Because the time complexity is O(n), have to
        # use an dictionary or hashmap.
        # If the time complexity is O(nlog(n)),
        # we can sort nums first.
        dict = {}
        for i in nums:
            dict[i] = False

        longest = 0
        for i in nums:
            if dict[i] == True:
                 continue
            length = 1
            dict[i] = True

            # check the consecutivity of the right
            # side of the current key
            j = i+1
            while dict.has_key(j):
                dict[j] = True
                length += 1
                j += 1

            # check the consecutivity of the left
            # side of the current key
            j = i-1
            while dict.has_key(j):
                dict[j] = True
                length += 1
                j -= 1

            # check the longest length
            longest = max(longest, length)
            if longest == len(nums): break

        return longest
