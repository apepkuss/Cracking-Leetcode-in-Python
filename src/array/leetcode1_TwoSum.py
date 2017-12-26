

class Solution:
    """
    @ Linkedin, Uber, Airbnb, Facebook, Amazon, Microsoft, Apple, Yahoo, Dropbox, Bloomberg, Yelp, Adobe

    Hash Table, Array

    Given an array of integers, return indices of the two numbers such that they add up to a specific target.

    You may assume that each input would have exactly one solution.

    Example:
    Given nums = [2, 7, 11, 15], target = 9,

    Because nums[0] + nums[1] = 2 + 7 = 9,
    return [0, 1].
    """
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target): # O(n) time, O(n) space
        assert num is not None

        if len(num) < 2:
            return None

        # key: the element in num
        # value: the index of the element
        adict = {}

        for idx, elem1 in enumerate(num):
            elem2 = target - elem1

            if elem2 in adict:
                return adict[elem2], idx + 1

            adict[elem1] = idx + 1

        return None