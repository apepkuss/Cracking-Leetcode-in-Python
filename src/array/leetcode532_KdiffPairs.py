

class Solution(object):
    """
    @ Amazon
    
    Two pointers
    
    Given an array of integers and an integer k, you need to find the number of unique k-diff pairs in the array. 
    Here a k-diff pair is defined as an integer pair (i, j), where i and j are both numbers in the array and their 
    absolute difference is k.

    Example 1:
    Input: [3, 1, 4, 1, 5], k = 2
    Output: 2
    Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
    Although we have two 1s in the input, we should only return the number of unique pairs.
    
    Example 2:
    Input:[1, 2, 3, 4, 5], k = 1
    Output: 4
    Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).
    
    Example 3:
    Input: [1, 3, 1, 5, 4], k = 0
    Output: 1
    Explanation: There is one 0-diff pair in the array, (1, 1).
    
    Note:
    The pairs (i, j) and (j, i) count as the same pair.
    The length of the array won't exceed 10,000.
    All the integers in the given input belong to the range: [-1e7, 1e7].
    """

    #
    # This problem is similar with leetcode 1 twoSum problem. For this problem, there are three methods:
    #
    # The simplest method is to try each pair;
    #
    # The second method is to use two pointers to iterate the array, which is a solution with O(n) time and O(1) space;
    #
    # The third method is to use hash table, which can be solve the problem in O(n) time, but needs O(n) space.
    #

    def findPairs_twoPointers(self, nums, k):  # O(nlogn) time, O(1) space
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        if not nums or k < 0:
            return count

        nums.sort()

        p = 0
        while p < len(nums):
            q = p + 1

            while q < len(nums) and abs(nums[p] - nums[q]) < k:
                q += 1

            if q < len(nums) and abs(nums[p] - nums[q]) == k:
                count += 1

            while p + 1 < len(nums) and nums[p] == nums[p+1]:
                p += 1

            p += 1

        return count

    def findPairs_hashtable(self, nums, k):  # O(n) time, O(n) space
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        if not nums or k < 0:
            return count

        adict = {}

        for num in nums:
            if num not in adict:
                adict[num] = 1
            else:
                adict[num] += 1

        for key, value in adict.items():
            if k == 0:
                if value > 1:
                    count += 1
            else:
                if key + k in adict:
                    count += 1

        return count


if __name__ == "__main__":
    nums = [1, 3, 1, 5, 4]
    k = 0
    res = Solution().findPairs_hashtable(nums, k)
    print res