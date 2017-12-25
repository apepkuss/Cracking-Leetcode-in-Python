
class Solution(object):
    """
    @ Google, Zenefits, Microsoft, Apple, Yahoo, Dropbox, Adobe
    
    Binary Search, Array, Divide and Conquer

    There are two sorted arrays nums1 and nums2 of size m and n respectively. Find the median of the two sorted arrays.
    The overall run time complexity should be O(Log(m+n)).

    Example 1:
    nums1 = [1, 3]
    nums2 = [2]

    The median is 2.0
    Example 2:
    nums1 = [1, 2]
    nums2 = [3, 4]

    The median is (2 + 3)/2 = 2.5
    """

    # Median: In probability theory and statistics, a median is described as the number separating the higher half of a
    # sample, a population, or a probability distribution, from the lower half.
    #
    # The median of a **finite** list of numbers can be found by arranging all the numbers from lowest value to highest
    # value and picking the middle one. There are different conventions to take median of an array with even number of
    # elements, one can take the mean of the two middle values, or first middle value, or second middle value.

    # Method 1: Simply count while merging. The time complexity is O(m+n).
    # Suppose m+n=2k is an even number. The idea is to use Merge procedure of merge sort algorithm. Keep track of the count
    # while comparing two elements of two arrays. If count becomes k (for 2n elements), we have reached the median. Take
    # the advantage of the elements at indexes k-1 and k in the merged array.

    # Method 2: By comparing the medians of two sorted arrays. The time complexity is O(Log(m+n)).
    # The idea is to use divide-and-conquer to first find the median of each array, then compare them.
    # The algorithm is shown as below. **This idea works only when the two arrays have same size.
    #
    # 1. Calculate the medians m1 and m2 of the input arrays nums1 and nums2, respectively.
    #   a) If m1 and m2 both are equal then we are done. return m1 (or m2).
    #   b) If m1 > m2, then the median is present in one of the two sub-arrays: nums1[0:m/2+1], nums2[n/2:n]
    #   c) If m1 < m2, then the median is present in one of the two sub-arrays: nums1[m/2:m], nums2[0:n/2+1]
    # 2. Repeat the above process until size of both the two arrays becomes 2.
    # 3. If the size of the two arrays is 2, then median = (max(nums1[0],nums2[0]) + min(nums1[1], nums2[1]))/2.
    #
    # Example:
    #
    # ar1[] = {1, 12, 15, 26, 38}
    # ar2[] = {2, 13, 17, 30, 45}
    #
    # For above two arrays m1 = 15 and m2 = 17
    #
    # For the above ar1[] and ar2[], m1 is smaller than m2. So median is present in one of the following two sub-arrays:
    #
    # [15, 26, 38] and [2, 13, 17]
    #
    # Let us repeat the process for above two sub-arrays:
    #
    # m1 = 26 m2 = 13. m1 is greater than m2. So the sub-arrays become
    #
    # [15, 26] and [13, 17]
    #
    # Now size is 2, so median = (max(ar1[0], ar2[0]) + min(ar1[1], ar2[1]))/2
    #                          = (max(15, 13) + min(26, 17))/2
    #                          = (15 + 17)/2
    #                          = 16
    #

    # recursive binary search
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        total = len(nums1) + len(nums2)

        if total & 1:
            # odd case
            return self.find_kth(nums1, nums2, total/2+1)
        else:
            # even case
            return (self.find_kth(nums1, nums2, total/2) + self.find_kth(nums1, nums2, total/2+1)) / 2.0

    def find_kth(self, nums1, nums2, k):
        """
        Find the k-th smallest element in nums1 + nums2
        :param nums1: sorted array
        :param nums2: sorted array
        :param k: the k-th smallest
        """
        # always assume the length of nums1 is less than that of nums2
        if len(nums1) > len(nums2):
            return self.find_kth(nums2, nums1, k)

        if len(nums1) == 0:
            return nums2[k-1]

        # base case:
        if k == 1:
            return min(nums1[0], nums2[0])

        # recursive step:
        n1 = min(k/2, len(nums1))
        n2 = k - n1

        # compare the n1-th element in nums1 with the n2-th element in nums2
        if nums1[n1-1] < nums2[n2-1]:
            return self.find_kth(nums1[n1:], nums2[:n2], k-n1)
        elif nums1[n1-1] > nums2[n2-1]:
            return self.find_kth(nums1[:n1], nums2[n2:], k-n2)
        else:
            return nums1[n1-1]

    # linear search
    def findMedianSortedArray_linear(self, nums1, nums2):
        assert nums1 is not None
        assert nums2 is not None

        m, n = len(nums1), len(nums2)

        if m == 0 and n == 0:
            return 0.
        elif m == 0:
            if n & 0x1:
                return nums2[n / 2]
            else:
                return (nums2[n / 2 - 1] + nums2[n / 2]) * 0.5
        elif n == 0:
            if m & 1:
                return nums1[m / 2]
            else:
                return (nums1[m / 2 - 1] + nums2[n / 2]) * 0.5
        else:
            if m > n:
                return self.findMedianSortedArray_linear(nums2, nums1)

            idx = (m + n) / 2 - 1
            print('idx: ', idx)

            is_odd = False
            if (m + n) & 1:
                is_odd = True
            print("is odd: ", is_odd)

            res = 0
            i = j = 0
            while i < m and j < n:
                print('i: %d, j: %d, idx: %d' % (i, j, idx))

                if (i + j + 2) == idx + 1:
                    res = min(nums1[i], nums2[j])
                    if not is_odd:
                        if i + 1 < m:
                            res += min(nums1[i + 1], nums2[j])
                        else:
                            res += nums2[j]
                        res *= 0.5
                    break

                elif (i + j + 2) < idx + 1:
                    if nums1[i] <= nums2[j]:
                        i += 1
                    else:
                        j += 1

                else:
                    return -1

            while j < n and (i + j + 1) < idx:
                j += 1

            res = nums2[j]
            if not is_odd:
                res = (res + nums2[j + 1]) * 0.5

            return res
