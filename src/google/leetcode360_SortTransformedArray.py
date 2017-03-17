
class Solution(object):
    """
    @Google

    Given a sorted array of integers nums and integer values a, b and c. Apply a function of the form
    f(x) = ax2 + bx + c to each element x in the array.

    The returned array must be in sorted order.

    Expected time complexity: O(n)

    Example:
    nums = [-4, -2, 2, 4], a = 1, b = 3, c = 5,

    Result: [3, 9, 15, 33]

    nums = [-4, -2, 2, 4], a = -1, b = 3, c = 5

    Result: [-23, -5, 1, 7]
    """
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        def f(x, a, b, c):
            return a * ( x **2) + b* x + c

        n = len(nums)
        res = []
        if a > 0:
            k = -b / (2 * a * 1.0)
            i = 0
            while i < n and nums[i] < k:
                i += 1
            i, j = i - 1, i
            while i >= 0 and j < n:
                if k - nums[i] <= nums[j] - k:
                    res.append(f(nums[i], a, b, c))
                    i -= 1
                else:
                    res.append(f(nums[j], a, b, c))
                    j += 1
            while i >= 0:
                res.append(f(nums[i], a, b, c))
                i -= 1
            while j < n:
                res.append(f(nums[j], a, b, c))
                j += 1
        elif a < 0:
            k = -b / (2 * a * 1.0)
            i, j = 0, n - 1
            while i <= j:
                if k - nums[i] >= nums[j] - k:
                    res.append(f(nums[i], a, b, c))
                    i += 1
                else:
                    res.append(f(nums[j], a, b, c))
                    j -= 1
        elif b > 0:
            for i in range(n):
                res.append(f(nums[i], a, b, c))
        elif b < 0:
            for i in range(n - 1, -1, -1):
                res.append(f(nums[i], a, b, c))
        else:
            res = [c] * n
        return res
