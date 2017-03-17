
class Solution(object):
    """
    @ Amazon

    Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return
    the maximum number. The time complexity must be in O(n).

    Example 1:
    Input: [3, 2, 1]

    Output: 1

    Explanation: The third maximum is 1.
    Example 2:
    Input: [1, 2]

    Output: 2

    Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
    Example 3:
    Input: [2, 2, 3, 1]

    Output: 1

    Explanation: Note that the third maximum here means the third maximum distinct number.
    Both numbers with value 2 are both considered as second maximum.

    Analysis:

    For finding k-th largest or smallest element in an array, there are usually three methods:
    1. Method 1: first sorting, then return the element at the target index. The time complexity is O(nlogn) for sorting.
    2. Method 2: construct a max heap (or, min heap), then do k times of extract operation on the heap. The time
                 complexity is O(nlogn) for building up the heap.
    3. Method 3: make use of the partition part in classic QuickSort algorithm. The time complexity is O(n) on average.

    """
    def thirdMax(self, nums):  # O(n) time on average, O(n) space for filtering out the potential duplicates
        """
        :type nums: List[int]
        :rtype: int
        """
        arr = list(set(nums))
        n = len(arr)
        if n == 0:
            return 0
        if n < 3:
            import sys
            res = -sys. maxint -1
            for num in arr:
                res = max(res, num)
            return res

        return self.kLargest(arr, 0, n- 1, 3)

    def kLargest(self, arr, left, right, k):
        pos = self.partition(arr, left, right)
        if right - pos == k - 1:
            return arr[pos]
        if right - pos > k - 1:
            return self.kLargest(arr, pos + 1, right, k)
        return self.kLargest(arr, left, pos - 1, k - pos + right - 1)

    def partition(self, arr, left, right):
        pivot = arr[right]
        i = left
        for j in range(left, right):
            if arr[j] < pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[i], arr[right] = arr[right], arr[i]
        return i