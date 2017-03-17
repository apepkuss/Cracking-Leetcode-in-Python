
class Solution(object):
    """
    Given two arrays, write a function to compute their intersection.

    Example: Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].
    """
    def intersect_hash(self, nums1, nums2):  # O(m+n) time, O(m) space
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dict = {}
        for x in nums1:
            if not dict.has_key(x):
                dict[x] = 1
            else:
                dict[x] += 1
        res = []
        for y in nums2:
            if dict.has_key(y) and dict[y ] >0:
                dict[y ] -=1
                res.append(y)
        return res

    def intersect_Sort_DoublePtr(self, nums1, nums2):  # O(max(mlogm, nlogn)) time, O(1) space
        nums1.sort()
        nums2.sort()
        i = j = 0
        res = []
        while i< len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                res.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return res