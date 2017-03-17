
class Solution(object):
    def fourSum_hash(self, nums, target):    # O(n^2) time
        nums.sort()
        n = len(nums)
        res = set()
        dict = {}
        # establish the dict
        for i in xrange(n-1):
            for j in xrange(i+1, n):
                sum = nums[i]+nums[j]
                # there could be duplicates
                if dict.has_key(sum):
                    dict[sum].append((i,j))
                else:
                    dict[sum] = [(i,j)]
        for i in xrange(n-4+1):
            for j in xrange(i+1, n-4+2):
                newsum = target - nums[i] - nums[j]
                if dict.has_key(newsum):
                    for item in dict[newsum]:
                        # Elements in a quadruplet (a,b,c,d)
                        # must be in non-descending order
                        if j < item[0]:
                            res.add((nums[i],nums[j],nums[item[0]],nums[item[1]]))

        return [list(t) for t in res]

    # Generic algorithm, which has O(n^3) running time.
    def fourSum_Generic(self, nums, target): # TLE error
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def ksum(nums, k, target):
            result = set()
            i = 0

            if k==2:
                j=len(nums)-1
                while i<j:
                    if nums[i]+nums[j] == target:
                        result.add((nums[i],nums[j]))
                    elif nums[i]+nums[j] > target:
                        j-=1
                    else:
                        i+=1
            else:   # case: k>2
                while i < len(nums)-k+1:
                    newtarget = target - nums[i]
                    subresult = ksum(nums[i+1:], k-1, newtarget)
                    if subresult:
                        result = result | set((nums[i],)+nr for nr in subresult)
                    i+=1
            return result

        nums.sort()
        return [list(t) for t in ksum(nums, 4, target)]
