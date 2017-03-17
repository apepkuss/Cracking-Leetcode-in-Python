import unittest

class Elements(object):
    """
    elements 14.2:

    Write a function which takes as input two sorted arrays of integers, and updates the first
    to the combined entries of the two arrays in sorted order. Assume the first array has enough
    empty entries at its end to hold the result.
    """

    @classmethod
    def merge_in_place(cls, nums1, m, nums2, n):
        """
        Merge two sorted arrays
        :param nums1: the first sorted array
        :param m: the number of elements in nums1
        :param nums2: the second sorted array
        :param n: the number of elements in nums2
        """
        i, j, k = m-1, n-1, m+n-1
        while i>=0 and j>=0:
            if nums1[i] >= nums2[j]:
                nums1[k] = nums1[i]
                k -= 1
                i -= 1
            else:
                nums1[k] = nums2[j]
                k -= 1
                j -= 1
        if j > 0:
            nums1[0:k+1] = nums2[0:j+1]

class TestRun(unittest.TestCase):

    def test_case1(self):
        nums1 = [2,3,5,9,11,0,0,0,0,0,0,0,0,0,0]
        nums2 = [2,5,6,8,9,10,12,13,15]
        Elements.merge_in_place(nums1, 5, nums2, 9)
        unittest.TestCase.assertEqual(self, first=[2,2,3,5,5,6,8,9,9,10,11,12,13,15,0], second=nums1)

    def test_case2(self):
        nums1 = [2, 3, 5, 6, 9, 11, 0, 0, 0, 0, 0, 0]
        nums2 = [6, 8, 10]
        Elements.merge_in_place(nums1, 6, nums2, 3)
        unittest.TestCase.assertEqual(self, first=[2, 3, 5, 6, 6, 8, 9, 10, 11, 0, 0, 0], second=nums1)


if __name__ == "__main__":
    unittest.main()

