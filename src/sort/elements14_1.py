import unittest

class Elements(object):
    """
    elements 14.1:

    Given two sorted arrays, return a new array containing elements common
    to the two arrays. You can assume that the input arrays are free of duplicates.
    """

    @classmethod
    def compute_intersection(cls, nums1, nums2):  # O(len(nums1)+len(nums2)) time
        """
        The following algorithm is the best solution when the array lengths are similar.

        :param nums1: the first sorted array
        :param nums2: the second sorted array
        :return: the new array containing elements common to nums1 and nums2
        """
        res = []
        if len(nums1)==0 or len(nums2)==0:
            return res
        i = j = 0
        while i<len(nums1) and j<len(nums2):
            if nums1[i] == nums2[j]:
                res.append(nums1[i])
                i += 1
                j += 1
            else:
                if nums1[i] < nums2[j]:
                    i += 1
                else:
                    j += 1
        return res

class RunTest(unittest.TestCase):

    def setUp(self):
        self.nums1 = None
        self.nums2 = None

    def test_case1(self):
        self.nums1 = [2, 3, 5, 9, 11]
        self.nums2 = [2, 5, 6, 7, 8, 9, 10, 12]
        res = Elements.compute_intersection(self.nums1, self.nums2)
        unittest.TestCase.assertEqual(self, first=[2,5,9], second=res)


if __name__ == "__main__":
    unittest.main()
