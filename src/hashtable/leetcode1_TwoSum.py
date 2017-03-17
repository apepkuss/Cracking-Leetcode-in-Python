

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
        dict = {} # key is the element in num, value is the index of the element in num.
        for i in range(len(num)):
            diff = target - num[i]
            if diff in dict:
                return dict[diff], i
            dict[num[i]] = i
        return -1, -1