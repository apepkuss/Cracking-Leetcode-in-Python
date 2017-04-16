import unittest
import sys


class Solutions(object):
    """
    Find the kth largest element in an unsorted array.
    Note that it is the kth largest element in the sorted order, not the kth distinct element.
    """

    # Method 1: quick-select algorithm in O(n) time
    @classmethod
    def find_kthMaxValue_ByQuickSelect(cls, arr, k): # O(n) time
        n = len(arr)
        if n == 1: return arr[0]

        # quick-select algorithm returns the k-th smallest element, so we need to
        # set the fourth argument as n-k, meaning it returns the (n-k) smallest
        # element, namely the k-th largest element in the array.
        return cls.quick_select(arr, 0, n-1, n-k)

    @classmethod
    def quick_select(cls, arr, low, high, k):  # average: O(n) time
        """
        Find the kth smallest element in arr between low and high indices.
        """
        if low <= k <= high:
            # each partition can make sure one element at p position, which is the p-th smallest element 
            p = cls.partition(arr, low, high)
            if p == k:
                return arr[p]
            if p < k:
                return cls.quick_select(arr, p+1, high, k)
            if p > k:
                return cls.quick_select(arr, low, p-1, k)
        return sys.maxint

    @classmethod
    def partition(cls, arr, low, high):
        pivot = arr[high]
        i = low
        for j in xrange(low, high):
            if arr[j] <= pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[i], arr[high] = arr[high], arr[i]
        return i



    # Method 2: sort the array first, then find the (n-k)th element. O(nlogn) time
    @classmethod
    def find_kthMaxValue_BySort(cls, arr, k): # O(nlogn) time
        arr.sort()
        return arr[k-1]



    # Method 3: max heap: O(n) for extraction, but O(nlogn) for building up heap and O(logn) for heapifying.
    @classmethod
    def find_kthMaxValue_ByMaxHeap(cls, arr, k):  # O(nlogn) time

        # Build up a max heap from the array
        max_heap = cls.build_maxHeap(arr)
        for _ in xrange(k-1):
            _, max_heap = cls.extract_maxValue(max_heap)
        return cls.extract_maxValue(max_heap)[0]

    @classmethod
    def build_maxHeap(cls, arr):  # O(n) time, even though the worst case complexity looks like O(nlogn).
        harr = arr
        i = (len(arr)-1)/2
        while i >= 0:
            harr = cls.maxHeapify(harr, i)
            i -= 1
        return harr

    @classmethod
    def maxHeapify(cls, harr, i):  # O(logn) time
        left = 2*i+1
        right = 2*i+2
        largest = i
        if left < len(harr) and harr[left] > harr[largest]:
            largest = left
        if right < len(harr) and harr[right] > harr[largest]:
            largest = right
        if largest != i:
            harr[i], harr[largest] = harr[largest], harr[i]
            harr = cls.maxHeapify(harr, largest)
        return harr

    @classmethod
    def extract_maxValue(cls, arr):  # O(logn) time
        # cache the root of current heap
        value = arr[0]

        # remove current root, and then heapify the left nodes to get a new heap
        arr[0] = arr[len(arr)-1]
        arr = arr[:len(arr)-1]
        arr = cls.maxHeapify(arr, 0)

        # return the max value and new heap
        return value, arr



    # Method 5: use built-in heapq to build up a min heap, then pop out the k-th largest element
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import heapq
        heap = []

        # push all elements into the min heap
        for num in nums:
            heapq.heappush(heap, num)

        # pop up the first (n-k) smallest elements
        for _ in range(len(nums) - k):
            heapq.heappop(heap)

        return heapq.heappop(heap)




class TestRun(unittest.TestCase):

    def test_case1(self):
        arr = [5,4,3,2,1]
        res = Solutions.find_kthMaxValue_ByQuickSelect(arr, 2)
        unittest.TestCase.assertEqual(self, first=4, second=res)

    def test_case2(self):
        arr = [-1,2,0]
        res = Solutions.find_kthMaxValue_ByMaxHeap(arr, 3)
        unittest.TestCase.assertEqual(self, first=-1, second=res)


if __name__ == "__main__":
    unittest.main()