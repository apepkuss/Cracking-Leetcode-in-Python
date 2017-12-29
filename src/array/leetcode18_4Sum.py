
class Solution(object):
    """
    Given an array S of n integers, are there elements a, b, c, and d in S such that
    a + b + c + d = target? Find all unique quadruplets in the array which gives
    the sum of target. Note:
    Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a+b+c+d)
    The solution set must not contain duplicate quadruplets.
    For example, given array S = {1, 0, -1, 0, -2, 2}, and target = 0. A solution set
    is: (-1, 0, 0, 1) (-2, -1, 1, 2) (-2, 0, 0, 2)
    """
    def fourSum_hash(self, nums, target):    # O(n^2) time
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        assert nums is not None

        nums.sort()
        n = len(nums)

        res = set()
        adict = {}

        # fill in adict
        for i in xrange(n-1):
            for j in xrange(i+1, n):
                asum = nums[i]+nums[j]

                if asum not in adict:
                    adict[asum] = [(i, j)]
                else:
                    adict[asum].append((i, j))

        for i in xrange(n-4+1):
            for j in xrange(i+1, n-4+2):
                val = target - nums[i] - nums[j]
                if val in adict:
                    for s, t in adict[val]:
                        # Elements in a quadruplet (a,b,c,d)
                        # must be in non-descending order
                        if j < s:
                            res.add((nums[i], nums[j], nums[s], nums[t]))

        return [list(t) for t in res]

    # Generic algorithm, which has O(n^3) running time.
    def fourSum_Generic(self, nums, target): # TLE error
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def ksum(nums, k, target):
            res = set()
            i = 0

            # base case
            if k == 2:
                j = len(nums)-1
                while i < j:
                    asum = nums[i] + nums[j]
                    if asum == target:
                        res.add((nums[i], nums[j]))
                    elif asum > target:
                        j -= 1
                    else:
                        i += 1

            # recursive step
            else:
                while i < len(nums) - k + 1:
                    newtarget = target - nums[i]
                    subresult = ksum(nums[i+1:], k-1, newtarget)
                    if subresult:
                        res = res | set((nums[i],)+nr for nr in subresult)
                    i += 1

            return res

        assert nums is not None
        nums.sort()
        res = ksum(nums, 4, target)
        return [list(t) for t in res]
