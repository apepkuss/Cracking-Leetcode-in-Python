
class Solution(object):
    def maxNumber_stack(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        m, n = len(nums1), len(nums2)
        res = []
        for i in xrange(k+1):
            j = k- i
            if i > m or j > n:
                continue
            tmp1 = self.getMax(nums1, i)
            tmp2 = self.getMax(nums2, j)
            # merge tmp1 and tmp2 into the largest sequence
            tmp = [max(tmp1, tmp2).pop(0) for _ in tmp1 + tmp2]
            res = max(res, tmp)
        return res

    def getMax(self, nums, k):
        """
        get the k-length largest sequence in nums
        """
        stack = []
        size = len(nums)
        for x in range(size):
            while stack and size - x > k - len(stack) and stack[-1] < nums[x]:
                stack.pop()
            if len(stack) < k:
                stack.append(nums[x])
        return stack

    def maxNumber_DP(self, nums1, nums2, k):
        if not k or len(nums1) + len(nums2) < k: return []

        loc1 = [[-1] * 10 for _ in range(len(nums1) + 1)]
        loc2 = [[-1] * 10 for _ in range(len(nums2) + 1)]
        l12 = len(nums1) + len(nums2)
        vis, res = set(), [-1] * k

        def make(nums, loc):
            pos = [-1] * 10
            for i in xrange(len(nums) - 1, -1, -1):
                pos[nums[i]] = i
                for j in range(10):
                    loc[i][j] = pos[j]

        make(nums1, loc1)
        make(nums2, loc2)

        def compare(p1, p2):
            if p2 == len(nums2): return 1
            if p1 == len(nums1): return 2
            if nums1[p1] > nums2[p2]: return 1
            if nums1[p1] < nums2[p2]: return 2
            return compare(p1 + 1, p2 + 1)

        def dfs(p1, p2, k):
            if k == 0 or (p1, p2, k) in vis: return

            if l12 == p1 + p2 + k:
                flag, update = True, False
                while flag and k > 0:
                    if compare(p1, p2) == 1:
                        if res[-k] <= nums1[p1] or update:
                            if res[-k] < nums1[p1]: update = True
                            res[-k] = nums1[p1]
                            p1 += 1
                        else:
                            flag = False
                    else:
                        if res[-k] <= nums2[p2] or update:
                            if res[-k] < nums2[p2]: update = True
                            res[-k] = nums2[p2]
                            p2 += 1
                        else:
                            flag = False
                    k -= 1
            else:
                flag = False
                for i in range(9, -1, -1):
                    if loc1[p1][i] != -1:
                        if l12 - loc1[p1][i] - p2 >= k and res[-k] <= i:
                            if res[-k] < i: res[-k:] = [-1] * k
                            res[-k] = i
                            dfs(loc1[p1][i] + 1, p2, k - 1)
                            flag = True
                    if loc2[p2][i] != -1:
                        if l12 - p1 - loc2[p2][i] >= k and res[-k] <= i:
                            if res[-k] < i: res[-k:] = [-1] * k
                            res[-k] = i
                            dfs(p1, loc2[p2][i] + 1, k - 1)
                            flag = True
                    if flag: break
            vis.add((p1, p2, k))

        dfs(0, 0, k)
        return res


if __name__ == "__main__":
    nums1 = [3,4,6,5]
    nums2 = [9,1,2,5,8,3]
    res = Solution().maxNumber_DP(nums1, nums2, k=5)
    print res
