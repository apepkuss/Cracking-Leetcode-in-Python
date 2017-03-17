
import heapq

class Solution(object):
    """
    @ Google, Uber

    You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.

    Define a pair (u,v) which consists of one element from the first array and one element from the second array.

    Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.
    """
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        if len(nums1) == 0 or len(nums2) == 0:
            return res
        heap = []
        m, n = len(nums1), len(nums2)
        # push all pairs consisting of nums1[i] and nums2[0] into the heap
        for i in range(m):
            heapq.heappush(heap, (nums1[i] + nums2[0], i, 0))

        while len(res) < min(k, m*n):
            asum, i, j = heapq.heappop(heap)
            res.append([nums1[i], nums2[j]])
            if j + 1 < n:
                heapq.heappush(heap, (nums1[i] + nums2[j+1], i, j+1))
        return res

    def kSmallestPairs_2(self, nums1, nums2, k):
        res = []
        if len(nums1) == 0 or len(nums2) == 0:
            return res
        m, n = len(nums1), len(nums2)
        heap = []
        heapq.heappush(heap, (nums1[0] + nums2[0], 0, 0))
        while len(heap) > 0 and len(res) < min(k, m * n):
            _, i, j = heapq.heappop(heap)
            res.append([nums1[i], nums2[j]])
            if j + 1 < n:
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
            if j == 0 and i + 1 < m:
                heapq.heappush(heap, (nums1[i + 1] + nums2[0], i + 1, 0))
        return res
