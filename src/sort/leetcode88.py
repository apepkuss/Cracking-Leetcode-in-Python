

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        x, y, z = m-1, n-1, m+n-1
        while x>=0 and y>=0:
            if nums1[x]<nums2[y]:
                nums1[z] = nums2[y]
                y-=1
            else:
                nums1[z] = nums1[x]
                x -= 1
            z -= 1
        if y >= 0:
            nums1[:y+1] = nums2[:y+1]
