import unittest


class Elements(object):
    """
    elements 14.4:

    Design an efficient algorithm for removing all the duplicates from an array.
    """

    @classmethod
    def remove_duplicates_sort(cls, nums):  # O(nlogn) time, O(1) space

        if len(nums) == 0:
            return nums

        nums.sort()  # O(nlogn) time

        slow, fast = 0, 0
        while fast < len(nums):
            if nums[slow] != nums[fast]:
                slow += 1
                nums[slow] = nums[fast]
            fast += 1

        return nums[:slow+1]

    @classmethod
    def remove_duplicates_list(cls, nums):  # O(n) time, O(n) space

        if len(nums) == 0:
            return nums

        res = []
        for num in nums:
            if num not in res:
                res.append(num)

        return res


class TestRun(unittest.TestCase):

    def test_case1(self):
        nums = [2, 1, 1, 3, 5, 2, 5, 5, 5, 3, 5]
        res = Elements.remove_duplicates_sort(nums)
        unittest.TestCase.assertEqual(self, first=[1, 2, 3, 5], second=res)

    def test_case2(self):
        nums = [2, 1, 1, 3, 5, 2, 5, 5, 5, 3, 5]
        res = Elements.remove_duplicates_list(nums)
        unittest.TestCase.assertEqual(self, first=[2, 1, 3, 5], second=res)


if __name__ == "__main__":
    unittest.main()